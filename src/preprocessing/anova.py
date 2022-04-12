import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols #ordinary least squares
import pandas as pd 

#read file with diag and demographics
df = pd.read_csv('phenotypesWithDemo.csv')

#show first 5 lines of my file
print(df.head(5))
print('----------------------------------------------------------')

#ols compute anova for Gender, Race and Ethnic

model = ols('DiagsNum ~ C(PTGENDER) +C(PTRACCAT) + C(PTETHCAT)', data=df).fit()
anova_result = sm.stats.anova_lm(model,typ=1)

#computes anova for Age (regression) dropping missing values
dfAge = df.dropna(subset=['Age'], how='all')
model2 = ols('DiagsNum ~ Age',data=dfAge).fit()
anova_result2 = sm.stats.anova_lm(model2,typ=1)

print("Anova for gender, race and ethnic: \n",anova_result)
print("Anova for age: \n", anova_result2)