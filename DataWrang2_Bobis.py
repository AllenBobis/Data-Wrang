import pandas as pd
dframe= {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension':['Length','Width','Height','Length','Width','Height'],
         'Value':[6,4,2,5,3,4]}
messy=pd.DataFrame(dframe,columns=['Box','Dimension','Value'])
tidy=messy.pivot(index='Box',columns='Dimension',values='Value').reset_index()
data= tidy[['Height','Length','Width']].transpose().prod().tolist()
vol1= {'Box':['Box1','Box2'],
         'Volume':data}
vol=pd.DataFrame(vol1,columns=['Box','Volume'])
tvol=pd.merge(tidy,vol,how='inner', on='Box')