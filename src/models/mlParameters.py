
import numpy as np
def mlParameters(model = None, x_train_shape = None, isGsRequest = False):
    if not isGsRequest:
        params = {
        'LogisticRegression' : {
            'max_iter' : 1000},

        'RandomForest' : {
            'random_state':42,
            'n_jobs' : -1
            }
        }
        return params.get(model,None)

    else:
        paramsGS = {
        'RandomForest' : {
            'n_estimators': [100, 250, 500, 1000,10000] #,100000,200000], #SQR da quantidade de de parametros
            #'max_features': [1, 2*np.sqrt(x_train.shape[1]), x_train.shape[1]*0.1, x_train.shape[1]*0.5, x_train.shape[1]],
            },

        'LogisticRegression' : {
            'C' : np.logspace(-4, 4, 20),
            'solver' : ["sag"]},
        
        'SVClassifier' : 
            {'C':[1,10,100,1000],
            'gamma':[1,0.1,0.001,0.0001],
            'kernel':['linear','rbf']}
        }
        return paramsGS.get(model,None)