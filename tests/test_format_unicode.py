# -*- coding: utf-8 -*-

from .context import arx_inf
from arx_inf.format_unicode import circ_codes, YearConvert

import unittest

class YearTestSuite(unittest.TestCase):
    """
    Test cases for year Unicode conversion.
    """
    def test_circ_code_dict(self):
        """
        Years between 2010-2050 (incl.) have circled Unicode
        representations, so here test that the circ_codes are all correct.
        """
        self.assertEqual([chr(circ_codes[x]) for x in range(10,51)],
        ['⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '㉑', '㉒',
        '㉓', '㉔', '㉕', '㉖', '㉗', '㉘', '㉙', '㉚', '㉛', '㉜', '㉝',
        '㉞', '㉟', '㊱', '㊲', '㊳', '㊴', '㊵', '㊶', '㊷', '㊸', '㊹',
        '㊺', '㊻', '㊼', '㊽', '㊾', '㊿'],
        [YearConvert(x) for x in range(2010,2051)])

    def test_default_to_tw(self):
        """
        Ensure the default ``to`` parameter remains set as ``tw``.
        """
        self.assertEqual(YearConvert(2018), YearConvert(2018, to="tw"))

    def test_integers(self):
        """
        Years pre-2009 don't get converted other than into strings.
        """
        self.assertEqual([YearConvert(x) for x in range(1900,2010)],
                         [str(x) for x in range(1900,2010)])

    def test_20c_year_abbrev(self):
        """
        Years for filenames don't get converted, the last two digits
        are used (may change this for 20C ambiguity in future? TBC).
        """
        self.assertEqual([YearConvert(x, to="log") for x in range(1960,2000)],
                         [str(x) for x in range(60,100)])

    def test_21c_year_abbrev(self):
        """
        Years for filenames in the 21st century, as above but
        handling 00 integers etc.
        """
        self.assertEqual([YearConvert(x, to="log") for x in range(2000,2050)],
               ['00'] + [f'0{x}' for x in range(1,10)] + \
               [str(x) for x in range(10,50)])

if __name__ == '__main__':
    unittest.main()
