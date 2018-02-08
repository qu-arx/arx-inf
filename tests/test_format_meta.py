from .context import arx_inf
from arx_inf import FormatAuth, FormatMeta
from .utils import AttrDict
import unittest

class AuthTestSuite(unittest.TestCase):
    """
    Test cases for author string formatting.
    """
    def test_one_author(self):
        assert FormatAuth(["Hello World"]) == "World"

    def test_two_authors(self):
        assert FormatAuth(["Hello World", "Foo B. Baz"]) == "World & Baz"

    def test_three_authors(self):
        assert FormatAuth(["Hello World", "Foo B. Baz",
        "Homer J. Simpson"]) == "World et al."

class MetaTestSuite(unittest.TestCase):
    """
    Test cases for metadata interpretation and formatting.
    """

    def test_tweet_format(self):
        test_metadata = AttrDict(dict(
            authors = ["Arthur Welt", "Foo B. Baz", "Homer J. Simpson"],
            title = "Testing",
            arxiv_primary_category = {'term': "CS.AI"},
            arxiv_url = "http://arxiv.org/abs/2001.12345v1",
            published_parsed = AttrDict(dict(tm_year = 2020)),
        ))
        assert FormatMeta(test_metadata) == "Welt et al. (⑳) Testing " \
        + "(arX⠶2001.12345v1［CS.AI］) http://arxiv.org/abs/2001.12345v1"

if __name__ == '__main__':
    unittest.main()
