import models.mlDispatcher as mlDispatcher
from models.mlEvaluate import Evaluate
import os, argparse, joblib
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import GridSearchCV,cross_validate
import numpy as np
from models.mlParameters import mlParameters
from sklearn.model_selection import cross_validate

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
        joblib.dump(self.model, f"../models/trained_{self.name}.joblib")

    def trainGS(self,x_train, y_train,doCV):
        """
        Train models using Grid Search to choose the best parameters
        """
        self.name += "GS"
        try:
            self.model = joblib.load(f"../models/trained_{self.name}_{self.dataName}.joblib")
        except:
            param_grid = mlParameters('RandomForest',isGsRequest= True)
                            
            self.model = GridSearchCV(estimator = self.model, param_grid = param_grid, scoring='recall', n_jobs=-1, cv=5, verbose=10)
            if doCV:
                cv_results = cross_validate(self.model, x_train, y_train, cv=10, scoring=['precision','recall','accuracy'],return_estimator=True,return_train_score=True,n_jobs=-1)
                cv_results_DF= pd.DataFrame(cv_results)
                cv_results_DF.to_csv("../models/trained_{self.name}_{self.dataName}.csv",index=False)
            else:
                self.model.fit(x_train,y_train)
                joblib.dump(self.model, f"../models/trained_{self.name}_{self.dataName}.joblib")


    def test(self, x_test, y_test, isGS):
        """
        Test ML model using metrics from mlEvaluate
        """
        y_predict = self.model.predict(x_test)
        prob_predict = self.model.predict_proba(x_test)
        print(y_test.to_list())
        print(y_predict)
        Evaluate(y_test,y_predict,prob_predict,self.dataName,self.isMulticlass,self.name) #is this APROPRIATE in OOP?

        return y_predict
