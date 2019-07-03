import pandas as pd
import xlrd

def dump_csv(filename):
    workbook = xlrd.open_workbook(filename)
    sheetNames = workbook.sheet_names()
    for sheetName in sheetNames:
        print(sheetName)
        outfilename = "%s.csv" % (sheetName)
        sheet_data = pd.read_excel(filename, sheetName, index_col = None)
        sheet_data.to_csv(outfilename, encoding = 'utf-8', index = False)

dump_csv('test_Tracking.xlsx')
