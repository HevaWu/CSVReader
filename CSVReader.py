import csv
from enum import Enum

from Error import Error

class CSVFileName(Enum):
    sheet1 = "HealthyFood.csv"
    sheet2 = "Weather.csv"

class CSVColumnName(Enum):
    name = "Name"
    types = "Types"
    category = "Category"
    location = "Location"
    weather = "Weather Forecasts"

class CSVReader():

    def __init__(self, filename):
        self.filename = filename
        self.dataSource = []
        self.fieldNames = []
        self._readCSVFile()

    @staticmethod
    def _formatArray(array):
        """Remove duplicate elements"""
        array = list(set(array))
        """Remove empty elements"""
        array = list(filter(None, array))
        return array

    def _readCSVFile(self):
        with open(self.filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            """Parse Column Name"""
            self.fieldNames = csv_reader.fieldnames
            for row in csv_reader:
                data = {}
                for csvName in CSVColumnName:
                    if csvName.value in self.fieldNames:
                        """Use .strip to remove \n"""
                        data[csvName.value] = str(row[csvName.value]).strip()
                if data:
                    self.dataSource.append(data)

    def getColumn(self, columnName):
        if columnName in self.fieldNames:
            column = [item[columnName] for item in self.dataSource]
            column = CSVReader._formatArray(column)
            print(column)
            return column
        else:
            raise Error("[CSVReader] '%s' is not exist in '%s' file" % (columnName, self.filename))

    def getDataSource(self):
        if self.dataSource:
            print(self.dataSource)
            return self.dataSource
        else:
            raise Error("[CSVReader] '%s' doesn't contain valid params. Please checking it again." % (self.filename))
