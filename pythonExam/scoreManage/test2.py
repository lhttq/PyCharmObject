import openpyxl
#创建工作表
wb = openpyxl.Workbook()
#定位工作表
ws = wb.active
wb.save("F:\lht\Desktop\8.xlsx")

