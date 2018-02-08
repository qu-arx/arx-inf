circ_codes = {
    10: 0x2469,
    11: 0x246A,
    12: 0x246B,
    13: 0x246C,
    14: 0x246D,
    15: 0x246E,
    16: 0x246F,
    17: 0x2470,
    18: 0x2471,
    19: 0x2472,
    20: 0x2473,
    21: 0x3251,
    22: 0x3252,
    23: 0x3253,
    24: 0x3254,
    25: 0x3255,
    26: 0x3256,
    27: 0x3257,
    28: 0x3258,
    29: 0x3259,
    30: 0x325A,
    31: 0x325B,
    32: 0x325C,
    33: 0x325D,
    34: 0x325E,
    35: 0x325F,
    36: 0x32B1,
    37: 0x32B2,
    38: 0x32B3,
    39: 0x32B4,
    40: 0x32B5,
    41: 0x32B6,
    42: 0x32B7,
    43: 0x32B8,
    44: 0x32B9,
    45: 0x32BA,
    46: 0x32BB,
    47: 0x32BC,
    48: 0x32BD,
    49: 0x32BE,
    50: 0x32BF
}

def YearConvert(y: int, to="tw") -> str:
    """
    Convert year from integer to the circled digit Unicode
    code point equivalent, if available (2010-2050).
    """
    if to == "tw":
        if 2009 < y < 2051:
            y = chr(circ_codes[y-2000])
        else:
            y = str(y)
    elif to == "log":
        y = str(y)[-2:]
    else:
        raise ValueError(f"Format {to} not recognised.")
    return y
