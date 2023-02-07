from openpyxl import workbook
from pandas import read_excel
sheet=[]
file="sales.xlsx"
i=1
for f in ['jan','feb','mar','apr']:
    df=""
    name='HCL_SALES_'+f
    df=df+str(i)
    df=read_excel(file,sheet_name=name,index_col=0)
    i+=1
    sheet.append(df)
dataframe=pd.concat(sheet)
print(dataframe)