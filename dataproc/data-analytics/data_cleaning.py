import pandas as pd
import numpy as np

"""
This is a generalized script for Data Cleaning, and can work for any dataset input
"""


# Method to Drop Multiple columns
def drop_columns(col_names, df):
    """
    Input -> (List of column names, dataset)
    """
    df.drop(col_names, axis=1, inplace=True)
    return df


# Method to change datatypes to save memory
def change_dtypes(col_int, col_float, df):
    """
    Input -> (column with integer, column with float, dataset)
    """
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')


# Change categorical to numerical
def change_cat_to_num(df):
    """
    Input -> dataset
    """
    num_encode = {'col_1': {'POSITIVE': 1, 'NEGATIVE': 0}}
    df.replace(num_encode, inplace=True)


# Checking for missing data
def check_missing_data(df):
    # Input is a dataset
    return df.isnull().sum().sort_values(ascending=False)


# Removing strings in columns to avoid errors
def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)

    # remove all the characters after &# (including &#) for column - col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)


# Remove whitespaces in columns
def remove_spaces(df, column):
    """
    Input -> dataset, column
    """
    # Strip the spaces from begininng of string
    df[column].str.lstrip()


# Manipulating timestamps - convert string to datetime format
def convert_str_datetime(df):
    """
    Input -> dataset
    """
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))
