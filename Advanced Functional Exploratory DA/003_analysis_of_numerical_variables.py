from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 600)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [
    col for col in df.columns if str(df[col].dtypes) in ["category ", "object", "bool"]
]

num_but_cat = [
    col
    for col in df.columns
    if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]
]

cat_but_car = [
    col
    for col in df.columns
    if df[col].nunique() > 20 and str(df[col].dtypes) in ["category ", "object"]
]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]


num_cols = [col for col in df.columns if df[col].dtypes in ["float64", "int64"]]
num_cols = [col for col in num_cols if col not in cat_cols]


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T) 

num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)


def num_summary(dataframe, numerical_col, plot = False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T) 
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)


for col in num_cols:
    num_summary(df, col, True)


def calc(wage, hour): 
    print(wage* hour) 
calc(10, 40)-200