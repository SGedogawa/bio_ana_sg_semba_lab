from mylib import calc

import pandas as pd
from gtfparse import read_gtf

if __name__ == '__main__':
    ima = calc.Calc().find_r_gene(3.0)
    print(len(ima))
