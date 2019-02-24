import openpyxl as xl
def col_to_list(col, rows):
    list = []
    for cell in col:
        c = cell[0]
        if c.value is None:
            break
        list.append(c.value)
    return list


wb = xl.load_workbook('name.xlsx')
# print(wb.sheetnames)
sheet=wb.get_active_sheet()
print(sheet.columns[1])





sheet1 = wb['Sheet1']
number_of_rows = sheet1.max_row

name_col = sheet1['a1':'a' + str(number_of_rows)]


name_list=col_to_list(name_col,number_of_rows)
ame_col
comp_col = sheet1['b1':'b' + str(number_of_rows)]
comp_list=col_to_list(comp_col,number_of_rows)

print(name_list)
print(comp_list)