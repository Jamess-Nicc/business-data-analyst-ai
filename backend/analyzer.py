import numpy as np
import pandas as pd


class LoadCsv:
    df = pd.read_csv("../data/sales.csv")
    print(df)


class RevenueSum:
    def __init__(self):
        self.revsum_out = None
