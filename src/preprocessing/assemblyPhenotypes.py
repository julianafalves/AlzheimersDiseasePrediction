from cmath import isnan, nan
from turtle import right
import pandas as pd
from sqlalchemy import column
import numpy as np
pheno = pd.read_csv('phenotypes.csv')
features = pd.read_csv('PTDEMOG.csv')
age = pd.read_csv('Individuos - ADNI1_Annual_2_Yr_1.5T_8_02_2019.csv',usecols=['Subject','Age'])

    
mydict={}
mylist = []
for i in features['RID']:
    zeros = (4 - len(str(i)))*'0'
    mydict[zeros + str(i)] = i

for i in pheno['Unnamed: 0.1']:
    #print(i[6:])
    #print('-------------------------------------------------------')
    keyname = i[6:]
    mylist.append(int(keyname))
    #print(keyname)
    #print(features[['PTGENDER','PTRACCAT','PTETHCAT','PTDOBYY']].loc[(features['RID']==mydict[keyname]) & (features['Phase']=='ADNI1')])
    #print(age.loc[age['Subject']==i])
pheno['featuresKey']= mylist
#print(pheno['featuresKey'])
#print (features['RID'])
features = features[features['Phase']=='ADNI1']
merged = pheno.merge(features[['RID','PTGENDER','PTRACCAT','PTETHCAT','PTDOBYY']], left_on='featuresKey',right_on ='RID')

merged['Age']=[2010-i for i in merged['PTDOBYY']]
merged.pop('PTDOBYY')
merged.pop('RID')
merged.pop('featuresKey')
merged.pop('Unnamed: 0')
merged['PTGENDER'] = [None if i == -4 else i for i in merged['PTGENDER']]
merged['PTRACCAT'] = [None if i == -4 else i for i in merged['PTRACCAT']]
merged['PTETHCAT'] = [None if i == -4 else i for i in merged['PTETHCAT']]

merged['DiagsNum']=[0 if i == 'CN' else 1 if i=='MCI' else 2 for i in merged['Diags']]
merged.to_csv('phenotypesWithDemo.csv',index=False)

print(merged)
