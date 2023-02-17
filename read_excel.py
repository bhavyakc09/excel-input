import sys
import pandas as pd

# Read data from Excel file
input_file = sys.argv[1]
data = pd.read_excel(input_file)

# Do something with the data, such as print it to the console
print(data)
