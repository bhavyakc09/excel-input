import sys
from openpyxl import load_workbook

excel_file_path = sys.argv[1]

workbook = load_workbook(filename=excel_file_path)
