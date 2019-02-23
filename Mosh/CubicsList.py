import openpyxl as xl


wb=xl.load_workbook('name.xlsx')
# print(wb.sheetnames)



sheet1=wb['Sheet1']

number_of_rows=sheet1.max_row

name=sheet1['a1':'a'+str(number_of_rows)]
for cell in name:
    c=cell[0]
    print(c.value)
print('-'*10)

comp = sheet1['b1':'b'+str(number_of_rows)]
for cell in comp:
    c=cell[0]
    if c.value is  None:
        break
    print(c.value)
