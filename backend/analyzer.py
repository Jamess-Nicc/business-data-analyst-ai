import numpy as np
import pandas as pd


class SalesAnalyzer:
    def load_data(self):
        self.df = pd.read_csv("../data/sales.csv")
        print(self.df)


class RevenueSum:
    def __init__(self, df):
        self.df = df
        self.revsum_calc = None
        self.avr_rev_calc = None

    def revsum_func(self):
        price = self.df["unit_price"]
        qty = self.df["quantity"]
        revsum_calc_operation = np.sum(price * qty)

        self.revsum_calc = revsum_calc_operation
        return revsum_calc_operation

    def avrgrev_func(self):
        total_revenue = self.revsum_func()
        avr_rev_operation = total_revenue / 15

        self.avr_rev_calc = avr_rev_operation
        return avr_rev_operation


analyzer = SalesAnalyzer()
analyzer.load_data()
revenue = RevenueSum(analyzer.df)
print(f"Total Revenue:  ₱{revenue.revsum_func()}")
average_revenue = RevenueSum(analyzer.df)
print(f"Average Revenue: ₱{average_revenue.avrgrev_func()}")
