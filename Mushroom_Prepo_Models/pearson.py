from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def split(xAll, yAll):

    X_train, X_test, y_train, y_test = train_test_split(xAll, yAll, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test


def create_pearson_matrix(df):
    pm = df.corr(method='pearson')
    return pm


def select_features(X_train, X_test):

    # Pearson Matrix is always calculated using Training Data 
    pm = create_pearson_matrix(X_train)

    # 'To be removed' list of columns (having high correlation with at least one other column)
    remove_cols = []

    for row in pm.iterrows():
        for col in pm.columns:

            # if both of the columns aren't already in the 'To be removed' list
            if row[0] not in remove_cols and col not in remove_cols:

                correlation = row[1][col]

                if row[0] != col:

                    # We chose the cutoff for high correlation to be 0.5
                    if abs(correlation) > 0.5:
                        remove_cols.append(col)
                        print(col)


    X_train = X_train.drop(columns = remove_cols)
    X_test = X_test.drop(columns = remove_cols)

    return X_train, X_test


def main():

    df = pd.read_csv('encoded_data.csv')
    df = df.iloc[: , 1:] # removing the first column which is just the index

    yAll = df['class']
    xAll = df.loc[:, df.columns != 'class']

    columns = xAll.columns


    ''' 
        Train-Test split
    '''
    xAll_numpy = xAll.to_numpy()
    yAll_numpy = yAll.to_numpy()
    X_train_numpy, X_test_numpy, y_train_numpy, y_test_numpy = split(xAll_numpy, yAll_numpy)

    X_train = pd.DataFrame(X_train_numpy, columns=columns)
    X_test = pd.DataFrame(X_test_numpy, columns=columns)
    y_train = pd.DataFrame(y_train_numpy, columns=['class'])
    y_test = pd.DataFrame(y_test_numpy, columns=['class'])



    '''
        Visualize the Pearson correlation matrix for Training and Testing Data
    '''
    corr_train = create_pearson_matrix(X_train)
    sns.heatmap(corr_train)
    plt.title("Pearson Correlation for Training Data")
    plt.savefig('pearsonmatrix-train.png')
    # plt.show()

    corr_test = create_pearson_matrix(X_test)
    sns.heatmap(corr_test)
    plt.title("Pearson Correlation for Testing Data")
    plt.savefig('pearsonmatrix-test.png')
    # plt.show()

    '''
        Dropping columns with high correlation with other columns
    '''
    X_train, X_test = select_features(X_train, X_test)

    '''
        Saving to csv file
    '''

    X_train.to_csv('xTrain.csv', index=False)
    X_test.to_csv('xTest.csv', index=False)
    y_train.to_csv('yTrain.csv', index=False)
    y_test.to_csv('yTest.csv', index=False)


if __name__ == '__main__':
    main()