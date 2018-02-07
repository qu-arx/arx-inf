# -*- coding: utf-8 -*-

from context import arx_inf
from arx_inf.format_unicode import circ_codes

import unittest

class YearTestSuite(unittest.TestCase):
    """
    Test cases for year Unicode conversion.
    """
    def test_circ_code_dict(self):
        """
        Years between 2010-2050 (incl.) have circled Unicode representations,
        so here test that the circ_codes are all correct.
        """
        assert [chr(circ_codes[x]) for x in range(10,51)] == ['⑩', '⑪', '⑫',
        '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '㉑', '㉒', '㉓', '㉔', '㉕',
        '㉖', '㉗', '㉘', '㉙', '㉚', '㉛', '㉜', '㉝', '㉞', '㉟', '㊱',
        '㊲', '㊳', '㊴', '㊵', '㊶', '㊷', '㊸', '㊹', '㊺', '㊻', '㊼',
        '㊽', '㊾', '㊿'] == [YearConvert(x) for x in range(2010,2051)]

    def test_integers(self):
        """
        Years pre-2009 don't get converted other than into strings.
        """
        assert [YearConvert(x) for x in range(1900,2010)] == \
                       [str(x) for x in range(1900,2010)]

if __name__ == '__main__':
    unittest.main()
