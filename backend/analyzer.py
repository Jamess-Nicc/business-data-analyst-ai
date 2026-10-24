import numpy as np
import pandas as pd
from scipy.stats import mode


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
        avr_rev_operation = total_revenue / 25

        self.avr_rev_calc = avr_rev_operation
        return avr_rev_operation


class CategoryAnalyzer:
    def __init__(self, df):
        self.df = df
        self.cat_most_shown = None

    def category_mode(self):
        category = self.df["category"]

        cat_mode_result = category.value_counts(dropna=False)

        self.cat_most_shown = cat_mode_result
        return cat_mode_result


analyzer = SalesAnalyzer()
analyzer.load_data()

revenue = RevenueSum(analyzer.df)
print(f"Total Revenue:  ₱{revenue.revsum_func()}")
average_revenue = RevenueSum(analyzer.df)
print(f"Average Revenue: ₱{average_revenue.avrgrev_func()}")

mode_of_category = CategoryAnalyzer(analyzer.df)
print(f"Most Frequent: {mode_of_category.category_mode()}")
