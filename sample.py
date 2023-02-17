import os
from openpyxl import load_workbook

excel_file_path = os.environ['EXCEL_FILE_PATH']

workbook = load_workbook(filename=excel_file_path)
