from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
from sklearn.linear_model import LogisticRegression


from models.mlParameters import mlParameters

models = {
    "RandomForest": RandomForestClassifier(**mlParameters('RandomForest')),
    #"XBoost":xgb.XGBClassifier(Parameters.XBoost),
    "LogisticRegression":  LogisticRegression(**mlParameters('LogisticRegression'))
}