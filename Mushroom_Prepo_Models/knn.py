import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

def knn(X_train, X_test, y_train, y_test):

    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    return y_pred


def main():


    X_train = pd.read_csv('xTrain.csv')
    X_test = pd.read_csv('xTest.csv')
    y_train = pd.read_csv('yTrain.csv')
    y_test = pd.read_csv('yTest.csv')

    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.to_numpy()
    y_test = y_test.to_numpy()

    y_pred = knn(X_train, X_test, y_train.ravel(), y_test.ravel())

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))



if __name__ == '__main__':
    main()