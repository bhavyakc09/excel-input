import os
print(os.getcwd())
from openpyxl import load_workbook

excel_file_path = os.environ['D:\demo\data.xlsx']

workbook = load_workbook(filename='D:/demo/data.xlsx')
