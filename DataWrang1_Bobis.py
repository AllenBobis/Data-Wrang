import pandas as pd
Math= {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
Electronics= {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
GEAS= {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
ESAT= {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
M=pd.DataFrame(Math,columns=['Student','Math'])
Elecs=pd.DataFrame(Electronics,columns=['Student','Electronics'])
G=pd.DataFrame(GEAS,columns=['Student','GEAS'])
E=pd.DataFrame(ESAT,columns=['Student','ESAT'])

a=pd.merge(M,Elecs,how='inner', on='Student')
b=pd.merge(a,G,how='inner', on='Student')
c=pd.merge(b,E,how='inner', on='Student')

lformat= c.melt(id_vars=['Student'], var_name='Subject', value_name='Grades')
lformat2= lformat.sort_values('Student')