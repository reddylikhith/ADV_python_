from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["product","sale","store"],
            [1,30,45],[2,34,56],[3,45,23],[4,67,21],[5,34,22]]
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=5,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("C://hcl1/product_chart.xlsx")