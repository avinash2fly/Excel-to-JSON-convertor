import json
import sys

import xlrd

excelFile = "abc.xls"
# e.g excelFile = "/Users/avinashgupta/Documents/abc.xlsx"

worksheet = "Sheet1"
#e.g worksheet = "Sheet1"


workbook = xlrd.open_workbook(excelFile)
worksheet = workbook.sheet_by_name(worksheet)

data = []
keysx = [v.value for v in worksheet.row(0)]
keys = [v.value for v in worksheet.row(1)]
for row_number in range(worksheet.nrows):
    if row_number < 2:
        continue
    row_data = {}
    for col_number, cell in enumerate(worksheet.row(row_number)):
        if keysx[col_number] in row_data:
            temp_data = row_data[keysx[col_number]]
        else:
            temp_data={}
        if keysx[col_number]=='N/A':
            row_data[keys[col_number]] = cell.value
        else:
            temp_data[keys[col_number]] = cell.value
            row_data[keysx[col_number]] = temp_data
    data.append(row_data)

with open("element.json", 'w') as json_file:
    json_file.write(json.dumps({'data': data}))