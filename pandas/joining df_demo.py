import pandas as pd
d1={'name':['pankaj','megh','lisaa'],'country':['india','usa','dubai']}
df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'id':[1,2,3],'name':['pankaj','anup','amit']})
print(df2)
df_merged=df1.merge(df2,how='left',on=df2['id'])
print(df_merged)