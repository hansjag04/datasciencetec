import pandas as pd

'''
Reads a CSV data file from an URL an returns
the matrix data separated from result.
'''
def get_data_from_url(url, labels=None):
    dataframe = pd.read_csv(url, names=labels)
    data_columns = dataframe.shape[1] - 1
    X = dataframe.iloc[:, 0:data_columns].values
    y = dataframe.iloc[:, data_columns].values
    return X, y

'''
Reads a CSV data file from an URL an returns
the matrix data separated from result.
'''
def get_data_from_url_without_first(url, labels=None):
    dataframe = pd.read_csv(url, usecols=[1,2,3,4,5,6,7,8], names=labels)
    # print(dataframe.head())
    data_columns = dataframe.shape[1] - 1
    X = dataframe.iloc[:, 0:data_columns].values
    y = dataframe.iloc[:, data_columns].values
    return X, y