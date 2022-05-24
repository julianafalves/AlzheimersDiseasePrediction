from sklearn.model_selection import train_test_split
import pandas as pd
from sympy import diag
from imblearn.over_sampling import SMOTE
from collections import Counter 
def toBinary(fenotypes,classes):
    '''
        Transform multiclass method to binary class

    '''
    class1,class2 = classes[0],classes[1]
    return fenotypes[(fenotypes['diag'] == class1) | (fenotypes['diag'] == class2)]

def preprocessing(isBinary, classes = []): 
    '''
        Pre processing steps for the genomic data. Including
            Transform txt file to dataframe  
                - Exclude space from subject to first snp
            Get phenotypes
            Select multiclass pr binary class option
    '''

    with open('genotiposPy') as f:
        lines = f.readlines()
    
    X = pd.DataFrame()
    data = []
    mapa = pd.read_csv('mapa',delimiter=' ') #get map file
    print(lines[0][0:30])
    #deletes space and \n
    for l in range(len(lines)):
        #lines[l] =lines[l].split(' ')
        '''while lines[l][11] == ' ':
            print(lines[l][11])
            print(lines[l][10])
            print(lines[0][0:30])
            lines[l].pop(10)'''
        #lines[l] = ' '.join(lines[l])
            
        lines[l] = lines[l].replace('       ',' ')
        lines[l] = lines[l].replace('\n','')

        data.append(lines[l].split(' '))
    
    X = pd.DataFrame(data) #dataframe with no header
    print(X.info())
    print(mapa.info())
    X.columns = ['subject']+ mapa['SNP_ID'].to_list() #dataframe with headers (so we can get variable inportance)
    
    X = X.set_index('subject') 
    del data #free memory space
    
    #Setting Y for my machine lear
    fenotipo = pd.read_csv('phenotypesNumeric.txt',delimiter = ' ',header=None)
    fenotipo.columns = ['subject','diag','ones']

    fenotipo = fenotipo.set_index('subject')
    if isBinary:
        fenotipo = toBinary(fenotipo,classes)
    
    y = fenotipo.loc[X.index.intersection(fenotipo.index),'diag'].astype(int)    
    X = X.loc[X.index.intersection(fenotipo.index),:].astype(int)
    del fenotipo #free memory space

    #oversampling dataset
    print(Counter(y))

    oversample = SMOTE()
    X,y = oversample.fit_resample(X,y)
    print(Counter(y))
    
    return X,y        

