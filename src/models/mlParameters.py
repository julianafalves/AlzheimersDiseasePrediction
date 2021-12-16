
import numpy as np

def mlParameters(model = None, shape = None):
    params = {
    'LogisticRegression' : {
        #'C' : np.logspace(-4, 4, 20),
        'solver' : "sag",
        'class_weight':'balanced'},

    'XBoost' : {
        # Parameters that we are going to tune.
        'max_depth':6,
        'min_child_weight': 1,
        'eta':.3,
        'subsample': 1,
        'colsample_bytree': 1,
        'eval_metric' : "mae",
        # Other parameters
        'objective':'reg:logistic'},

    'RandomForest' : {
        'n_estimators': int(10),
        #'max_features': [1, 2*np.sqrt(shape), shape*0.1, shape*0.5, X.shape[1]]
        }
    }

    return params.get(model,None)