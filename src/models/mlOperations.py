import models.mlDispatcher as mlDispatcher
from models.mlEvaluate import Evaluate
import os, argparse, joblib
import pandas as pd
from sklearn import metrics


class genericModel:
    def __init__(self,algorithm,dataName) -> None:
        """
        Build ML model, using de parameters from mlParameters
        """       
        self.model = mlDispatcher.models[f"{algorithm}"]
        self.name = algorithm
        self.dataName = dataName
        self.isMulticlass = True

    def train(self,x_train, y_train):
        """
        Train ML model and save joblib in "AlzheimersDisease/models"
        """
        self.model.fit(x_train,y_train)
        joblib.dump(self.model, f"models/trained_{self.name}.joblib")


    def test(self, x_test, y_test):
        """
        Test ML model using metrics from mlEvaluate
        """
        y_predict = self.model.predict(x_test)
        prob_predict = self.model.predict_proba(x_test)
        Evaluate(y_test,y_predict,prob_predict,self.dataName,self.isMulticlass,self.name) #is this APROPRIATE in OOP?

        return y_predict
