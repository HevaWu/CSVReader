import pandas as pd

from Error import Error
from CSVReader import CSVReader, CSVColumnName, CSVFileName

class Autogenerator():
    def __init__(self, filename):
        self.filename = filename
        self.generateSwiftFile()

    def _getCSVDataSource(self, csvFileName):
        rd = CSVReader(csvFileName)
        return rd.getDataSource()

    def dump_csv(self):
        workbook = pd.ExcelFile(self.filename)
        sheetNames = workbook.sheet_names
        for sheetName in sheetNames:
            print(sheetName)
            outfilename = "%s.csv" % (sheetName)
            sheet_data = pd.read_excel(self.filename, sheetName, index_col = None)
            sheet_data.to_csv(outfilename, encoding = 'utf-8', index = False)

    def generateSwiftFile(self):
        try:
            self.dump_csv()
            print("HealtyFood Sheet: ")
            print(self._getCSVDataSource(CSVFileName.sheet1.value))
            print("Weather Sheet: ")
            print(self._getCSVDataSource(CSVFileName.sheet2.value))
        except Error as e:
            print("Received Error: ", e.data)

Autogenerator('TestExcel.xlsx')
