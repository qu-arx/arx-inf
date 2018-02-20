from .context import arx_inf
from arx_inf import FormatAuth, FormatMeta
from .utils import test_metadata
import unittest

class AuthTestSuite(unittest.TestCase):
    """
    Test cases for author string formatting.
    """
    def test_default_style(self):
        """
        Confirm the default value of ``style`` parameter in ``FormatAuth``
        is set to "summary".
        """
        self.assertEqual(FormatAuth(["Test"]), \
                         FormatAuth(["Test"], style="summary"))
        
    def test_one_author(self):
        self.assertEqual(FormatAuth(["Hello World"]), "World")

    def test_two_authors(self):
        self.assertEqual(FormatAuth(["Hello World", "Foo B. Baz"]), \
                         "World & Baz")

    def test_three_authors(self):
        self.assertEqual(FormatAuth(["Hello World", "Foo B. Baz",
                         "Homer J. Simpson"]), "World et al.")

    def test_filename_auth_format(self):
        self.assertEqual(FormatAuth(["Hello World"], style="filename"), \
                         "world")

class MetaTestSuite(unittest.TestCase):
    """
    Test cases for metadata interpretation and formatting.
    """

    def test_tweet_format(self):
        self.assertEqual(FormatMeta(test_metadata),
            "Welt et al. (⑳) Testing (arX⠶2001.12345v1［CS.AI］)" + \
            " http://arxiv.org/abs/2001.12345v1")

    def test_log_format(self):
        self.assertEqual(FormatMeta(test_metadata, to="log"),
        "- [ ] welt20 ⠶ [Testing](http://arxiv.org/abs/2001.12345v1)")

if __name__ == '__main__':
    unittest.main()
