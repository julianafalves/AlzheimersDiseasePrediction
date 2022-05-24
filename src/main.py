from models.mlOperations import genericModel
from preprocessing import preprocessing
import os, argparse, joblib
import pandas as pd
from sklearn.model_selection import train_test_split

def pipeline (X,y,dataname, doCV= False):
    """
        Create a Machine Learning pipeline
            Implement a model constructor, train, test and evaluation
    """

    model = genericModel("RandomForest",dataname+f"_doCV_{doCV}")
    if doCV:
        model.trainGS(X, y,doCV=doCV)
    else:
        X_train, y_train,X_test,y_test= train_test_split(X, y, test_size=0.2, random_state=5)
        model.trainGS(X_train, y_train,doCV=doCV)
        model.test(X_test,y_test, isGS = True)

if __name__ == "__main__":
    #df = pd.read_csv("input/Iris.csv")
    #print(df.head())
    for runN in range(1,2):
       for ldValue in [80]:
        filePath = f"../ADNI1filtered/run{runN}/LD/LD{ldValue}"
        os.chdir(filePath)
        #data = preprocessing()
        print('im here')
        
        #pipeline(*data,f"run{runN}LD{ldValue}")
        dataName = f"run{runN}LD{ldValue}"
        data = preprocessing(isBinary= False)
        os.chdir('../../../..')
        os.chdir('src')
        print('im here2')
        pipeline(*data,dataName,doCV=True)

        for classes in [[0,1],[1,2],[0,2]]:
            os.chdir(filePath)
            data = preprocessing(isBinary= True,classes= classes)
            os.chdir('../../../..')
            os.chdir('src')
            pipeline(*data,dataname= dataName+f'{classes[0]}+{classes[1]}',doCV=True)
