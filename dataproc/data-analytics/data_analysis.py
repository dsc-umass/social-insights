from .data_cleaning import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = ""
df = pd.read_csv(path)

# Get the Data
def get_data():
    df.index = np.arange(1, len(df) + 1)
    return df

# View the first 'n' rows of data - typically multiples of 5
def view_data(n):
    return df.head(n)

def describe_data():
    return df.describe()

def count_unique(col):
    df[col].nunique()

