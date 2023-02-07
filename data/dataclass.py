from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class people():
    name:str
    num:int
    age:int
obj=[people('string',1,3),people('raju',34,5)]
data=[[p.name,p.num,p.age]for p in obj]
for d in data:
    sheet.append(d)
wb.save("dtclassdemo.xlsx")

#hcl_tech likhith reddy
#likhith reddy