import pandas as pd
df=pd.read_csv("C://hcl1/maths.csv")
#print(df)
df['Total']=df.iloc[:].sum(axis=1)
df['avg']=df['Total']/5
df['Rank']=df['avg'].rank()
print(df.sort_values(by=['Rank']))