from models.mlOperations import genericModel
from preprocessing import preprocessing
import os, argparse, joblib
import pandas as pd
from sklearn.model_seletion import train_test_split

def pipeline (X_train, X_test, y_train, y_test):
    """
        Create a Machine Learning pipeline
            Implement a model constructor, train, test and evaluation
    """

    model = genericModel("LogisticRegrssion")
    model.train(X_train, y_train)
    model.test(X_test,y_test)

if __name__ == "__main__":
    df = pd.read_csv("input/Iris")

    data = preprocessing(df)
    pipeline(*data)