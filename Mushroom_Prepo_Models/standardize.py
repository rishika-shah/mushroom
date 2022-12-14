import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


def normalize(xTrain, xTest):

    scaler = StandardScaler()
    scaler.fit(xTrain)

    xTrain_normalized = scaler.transform(xTrain)
    xTest_normalized = scaler.transform(xTest)

    return xTrain_normalized, xTest_normalized

def main():
    
    X_train = pd.read_csv('xTrain.csv')
    X_test = pd.read_csv('xTest.csv')
    y_train = pd.read_csv('yTrain.csv')
    y_test = pd.read_csv('yTest.csv')
    
    features = list(X_train.columns)
    
    X_train, X_test = normalize(X_train, X_test)
    
    X_train = pd.DataFrame(X_train, columns = features)
    
    X_test = pd.DataFrame(X_test, columns = features)
    
    X_train.to_csv("xTrain.csv", index=False)
    X_test.to_csv("xTest.csv", index=False)




if __name__ == '__main__':
    main()