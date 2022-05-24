from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV,cross_validate
from sklearn.svm import SVC

from models.mlParameters import mlParameters

models = {
    "RandomForest": RandomForestClassifier(**mlParameters('RandomForest')),
    #"XBoost":xgb.XGBClassifier(Parameters.XBoost),
    "LogisticRegression":  LogisticRegression(**mlParameters('LogisticRegression')),
    "SVClassifier": SVC()

}