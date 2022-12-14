import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

def normalize(df):

    scaler = StandardScaler()
    scaler.fit(df)

    df_normalized = scaler.transform(df)

    return df_normalized


    # for col_name in df.columns:

    #     col = df[col_name]
    #     datatype = col.dtype

    #     if datatype == 'float64':

    #         normalized_column = preprocessing.normalize([np.array(col)])
    #         df[col_name] = normalized_column[0]

    # return standardized

        

def main():

    df = pd.read_csv('encoded_data.csv')
    columns = df.columns

    df = normalize(df)
    df = pd.DataFrame(df, columns=columns)
    # print(df.head())
    # print(type(df))
    # print(df.shape)

    df.drop('Unnamed: 0', axis = 1, inplace = True)

    df.to_csv('standard_scaled_data.csv', index=False)


if __name__ == '__main__':
    main()