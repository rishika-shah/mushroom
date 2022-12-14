import pandas as pd

def handle_missing_values(df):

    for col_name in df.columns:

        col = df[col_name]
        datatype = col.dtype

        if datatype == 'object':

            ## for all missing values put majority class
            mode = col.mode()
            replacer = mode[0]

        if datatype == 'float64':

            ## for all missing values put mean
            replacer = col.mean()

        df[col_name] = df[col_name].fillna(replacer)

    return df



def main():

    df = pd.read_csv('secondary_data.csv', sep=';')
    # df = handle_missing_values(df)
    # df.to_csv('complete_data.csv')
    print(df.head())



if __name__ == '__main__':
    main()