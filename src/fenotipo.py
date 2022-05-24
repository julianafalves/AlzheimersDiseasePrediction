import pandas as pd
from sqlalchemy import column

fenotipo = pd.read_csv('../input/phenotypesNumeric.txt',delimiter = ' ',header=None)
fenotipo.columns = ['subject','diag','ones']
y = fenotipo.set_index('subject')
print(y)