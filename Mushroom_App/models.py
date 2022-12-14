import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.preprocessing import StandardScaler


xTrain = pd.read_csv('./data/rawxTrain.csv')
yTrain = pd.read_csv('./data/yTrain.csv')
xTrain = xTrain.to_numpy()
yTrain = yTrain.to_numpy()
classification_array = ["poisonous", "edible"]
scaler = StandardScaler()
scaler.fit(xTrain)
xTrain = scaler.transform(xTrain)


def knn_prediction(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(xTrain, yTrain)

    prediction = clf.predict([array])
    return classification_array[prediction[0]]


# Decision Tree


def dt_prediction(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    dt = tree.DecisionTreeClassifier()
    dt.fit(xTrain, yTrain)

    prediction = dt.predict(
        [array])
    return classification_array[prediction[0]]


# Naive Bayes


def NB_prediction(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    gnb = GaussianNB()

    prediction = gnb.fit(xTrain, yTrain).predict(
        [array])
    return classification_array[prediction[0]]

# Logistic Regression


def Logistic_Regression_prediction(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    clf = LogisticRegression(random_state=1, max_iter=1000).fit(xTrain, yTrain)

    prediction = clf.predict(
        [array])
    return classification_array[prediction[0]]

# Random Forest


def Random_Forest_prediction(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    clf = RandomForestClassifier(
        max_depth=2, random_state=0).fit(xTrain, yTrain)

    prediction = clf.predict(
        [array])
    return classification_array[prediction[0]]

# Support Vector Machines


def SVMachines(array):
    array = scaler.transform([array])
    array = array[0]
    # array = np.array(data_input)
    clf = svm.SVC().fit(xTrain, yTrain)

    prediction = clf.predict(
        [array])
    return classification_array[prediction[0]]


# def main():
#     # prediction = knn_prediction(1, 2, 1, 1)
#     # print(prediction)

#     prediction knn_prediction(1, 2, 3, 3)


# if __name__ == "__main__":
#     main()
