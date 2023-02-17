import sys
from openpyxl import load_workbook

excel_file_path = sys.argv[1]

workbook = load_workbook(filename=excel_file_path)

for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        if i.endswith(".xls") or i.endswith(".xlsx"):
            wb = openpyxl.load_workbook(os.path.join(os.getcwd(), i))
