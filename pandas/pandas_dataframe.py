import pandas as pd
d={'team':["ind","eng","nz"],'Rank':[1,2,3]}
df=pd.DataFrame(d)
#df.rename(columns={"Rank":"Ranking"},inplace=True)
#df.set_axis(df['team'],inplace=True)
#print(df.loc[df['Ranking']>=1])
print(df)
df.drop(['team'],axis=1,inplace=True)
print(df)
