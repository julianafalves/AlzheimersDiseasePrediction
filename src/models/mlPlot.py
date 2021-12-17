from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score, roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
import seaborn as sns
import numpy as np
from scipy import interp

def plotROC(y_test,prob_predict,dataName,isMulticlass,algorithm):
    '''
    Calculate and plot ROC curve, then save the image in 'results/figs/roc'
    '''
    n_class  = prob_predict.shape[1]
    fpr = dict()
    tpr = dict()
    thresh ={}
    roc_auc = dict()

    #calculate FPRs and TPRs and plot ROC curve
    plt.style.use('ggplot')
    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    for i in range(n_class):    
        fpr[i], tpr[i], thresh[i] = roc_curve(y_test, prob_predict[:,i], pos_label=i)
        roc_auc[i] = auc(fpr[i], tpr[i])
        plt.plot(fpr[i], tpr[i], linestyle='-', label=f'Class {i} vs Rest {round(roc_auc[i],2)}')

    if isMulticlass:
        #fpr["micro"], tpr["micro"], _ = roc_curve(np.array(y_test).ravel(), np.array(prob_predict).ravel())
        #roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
        #plt.plot(fpr["micro"], tpr["micro"], linestyle='-', label=f'Class micro  {(roc_auc["micro"])}')

        # First aggregate all false positive rates
        all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_class)]))

        # Then interpolate all ROC curves at this points
        mean_tpr = np.zeros_like(all_fpr)
        for i in range(n_class):
            mean_tpr += interp(all_fpr, fpr[i], tpr[i])

        # Finally average it and compute AUC
        mean_tpr /= n_class

        fpr["macro"] = all_fpr
        tpr["macro"] = mean_tpr
        roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
        
        plt.plot(fpr["macro"], tpr["macro"], linestyle='-', label=f'Class macro {round(roc_auc["macro"],2)}')
        
    title=f'{algorithm} - ({dataName})'
    plt.title(f'{title} ROC curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='best')
    plt.savefig(f'results/figs/roc/{title}',dpi=300)   
    plt.show()
