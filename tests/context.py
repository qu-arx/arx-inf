from sys import path as syspath
from pathlib import Path

inf = Path(__file__) / '..' / '..' / 'arx_inf'
syspath.insert(1, inf.resolve())

import arx_inf
