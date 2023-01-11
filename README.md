# Mushroom Edibility Predictor

This Flask web app that predicts the edibility of a mushroom sample using a mushroom sample's physical features.
The dataset used for this project is from the UCI Machine Learning repository, and can be found [here](https://archive.ics.uci.edu/ml/datasets/Secondary+Mushroom+Dataset).

### Machine Learning Models 

The following models are included in the project:

* K-Nearest Neighbors
* Decision Tree
* Logistic Regression
* Naive Bayes
* Random Forest
* Support Vector Machine

Eventually, the best model gave an accuracy, F-1 score and AUROC >99%. 

For details on preprocessing steps, models and empirical results, see the research paper - `mlpaper.pdf`.

All python scripts for preprocessing as well as each of the models can be found in the `Mushroom_Prepo_Models` folder, and all code for the Flask app can be found in the `Mushroom_App` folder. 


Created by Marcos Rivas, Rishika Shah, Rex Zhang - Fall 2022.
