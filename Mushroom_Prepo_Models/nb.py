import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

def nb(X_train, X_test, y_train, y_test):

    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    return y_pred


def main():

    X_train = pd.read_csv('xTrain.csv')
    X_test = pd.read_csv('xTest.csv')
    y_train = pd.read_csv('yTrain.csv')
    y_test = pd.read_csv('yTest.csv')

    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.to_numpy().ravel()
    y_test = y_test.to_numpy().ravel()

    y_pred = nb(X_train, X_test, y_train.ravel(), y_test.ravel())
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    print("F1:", f1_score(y_test, y_pred, average='weighted'))
    
#     clf = GridSearchCV(
#         KNeighborsClassifier(), 
#         [{'n_neighbors': range(1,17,5), 'metric': ['euclidean','manhattan']}], cv=5, scoring='accuracy')
    
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
    
#     print("Best parameters set found on development set:")
#     print(clf.best_params_)
#     print()
#     print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
#     print("F1:", f1_score(y_test, y_pred, average='micro'))
    



if __name__ == '__main__':
    main()