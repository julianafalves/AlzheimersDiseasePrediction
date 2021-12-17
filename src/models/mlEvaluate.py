from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score, roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
import pandas as pd

from models.mlPlot import plotROC

def Evaluate(y_test,y_predict,prob_predict,dataName,isMulticlass,algorithm):
    """
        Metrics for Ml evaluation
    """
    if isMulticlass:
        metrics = {'auc' : [roc_auc_score(y_test['class'].to_numpy(),prob_predict,multi_class='ovo', average='weighted')],
                'Accuracy' : [accuracy_score(y_test,y_predict)], 
                'Precision' : [precision_score(y_test,y_predict,average='micro')],
                'Recall' : [recall_score(y_test,y_predict, average='macro')],
                'F1 Score' : [f1_score(y_test,y_predict,average='micro')],
                }
    else:
        pass

    metrics_df = pd.DataFrame(metrics,columns=['auc','Accuracy','Precision','Recall','F1 Score'])

    '''
    Saving the metrics results into a csv file "results/metrics.csv"
    '''
    try:
        result_df = pd.read_csv("results/metrics.csv")
    except:
        result_df = pd.DataFrame(columns=['auc','Accuracy','Precision','Recall','F1 Score'])

    result_df= result_df.append(metrics_df,ignore_index=True)   
    result_df.to_csv("results/metrics.csv",index=False)
    
    #Plots
    plotROC(y_test,prob_predict,dataName,isMulticlass,algorithm)