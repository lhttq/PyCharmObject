import xlrd
def Excel(files ,rows, cols):#files:Excel文件的绝对路径；rows：起始行；cols：起始列
   # 打开文件
   x1 = xlrd.open_workbook(files)
   #输出第一个Sheet表格的名字
   print(x1.sheet_names()[0])
   #获取第一个Sheet表格的名字
   sheetName = x1.sheet_names()[0]
   #根据名字获取第一个sheet表格的内容
   content = x1.sheet_by_name(sheetName)
   #获取表格内容的所有行和列
   all_cols = content.ncols  # 列
   all_rows = content.nrows  # 行
   #循环输出表格的数据
   l = []
   for i in range(rows, all_rows - 2):
      num = content.cell(i, cols).value
      num1 = round(num, 2)
      l.append(num1)
   return l
l = Excel("F:\lht\Desktop\8-01.xlsx",2,8)
print(l)