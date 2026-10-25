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


class ProductAnalyzer:
    def __init__(self, df):
        self.df = df
        self.most_prod_shown = None

    def product_mode(self):
        product = self.df["product"]

        prod_mode_result = product.value_counts(dropna=False)

        self.most_prod_shown = prod_mode_result
        return prod_mode_result


class RevenueShareCategory:
    def __init__(self, df):
        self.df = df
        self.gross_sales_total = None
        self.net_rev_total = None

    def gross_sales_func(self):
        qty = self.df["quantity"]
        unit_price = self.df["unit_price"]

        gross_sales_calc = qty * unit_price

        self.gross_sales_total = gross_sales_calc
        return gross_sales_calc

    def net_rev_func(self):
        discounts = self.df["discount"]

        gross_sales_got = self.gross_sales_func()
        net_rev_calc = gross_sales_got - discounts

        self.net_rev_total = net_rev_calc
        return net_rev_calc


class GroupNetRevenueByCategory:
    def __init__(self, df, net_revenue):
        self.df = df
        self.net_revenue = net_revenue
        self.grouped_net_rev = None

    def group_net_rev(self):
        category = self.df["category"]

        grouped_calc = self.net_revenue.groupby(category).sum()

        self.grouped_net_rev = grouped_calc
        return grouped_calc


analyzer = SalesAnalyzer()
analyzer.load_data()

revenue = RevenueSum(analyzer.df)
print(f"Total Revenue:  ₱{revenue.revsum_func()}")
average_revenue = RevenueSum(analyzer.df)
print(f"Average Revenue: ₱{average_revenue.avrgrev_func()}")

mode_of_category = CategoryAnalyzer(analyzer.df)
print(f"Most Frequent: {mode_of_category.category_mode()}")

mode_of_product = ProductAnalyzer(analyzer.df)
print(f"Most Frequent:{mode_of_product.product_mode()}")

gross_sale_output = RevenueShareCategory(analyzer.df)
print(f"Gross Sales: {gross_sale_output.gross_sales_func()}")

net_rev_output = RevenueShareCategory(analyzer.df)
print(f"Net Revenue: {net_rev_output.net_rev_func()}")

revenue_analyzer = RevenueShareCategory(analyzer.df)

net_revenue = revenue_analyzer.net_rev_func()

category_analyzer = GroupNetRevenueByCategory(analyzer.df, net_revenue)

print(f"Grouped Net Revenue: {category_analyzer.group_net_rev()}")
