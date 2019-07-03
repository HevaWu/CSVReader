import csv

class CSVReader():
    @staticmethod
    def _formatArray(array):
        """Remove duplicate elements"""
        array = list(set(array))
        """Remove empty elements"""
        array = list(filter(None, array))
        """Remove \n from all elements"""
        array = list(map(str.strip, array))
        return array

    @staticmethod
    def _parseScreens(dataSource):
        screens = []
        for item in dataSource:
            screens.append(item[ScreenCSVReader.screenColumnName])
        screens = CSVReader._formatArray(screens)
        return screens

class ScreenCSVReader():
    screenColumnName = "screen"
    tsEventColumnName = "TS_event_name"

    def __init__(self):
        self.dataSource = []
        self.screens = []
        self.tsEventNameList = None
        self._readCSVFile()

    def _readCSVFile(self):
        with open('Screen.csv', mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            """Parse Data"""
            for row in csv_reader:
                self.dataSource.append(row)

        """Retrive Screen List"""
        self.screens = CSVReader._parseScreens(self.dataSource)

        """Retrieve TS Event Name"""
        self.tsEventName = self.dataSource[1]["TS_event_name"]

        """Format Screen Name List (remove duplicate & empty value)"""
        self.screens = CSVReader._formatArray(self.screens)

    def getScreens(self):
        print(self.screens)
        return self.screens

    def getTSEventName(self):
        print(self.tsEventName)
        return self.tsEventName

"""Read ClickEvent.csv or """
class ClickEventCSVReader():
    overViewColumnName = "overview"
    screenColumnName = "screen"
    actionColumnName = "action"
    labelColumnName = "label"
    tsEventColumnName = "TS_event_name"

    def __init__(self, filename):
        self.filename = filename
        self.dataSource = []
        self.tsEventName = None
        self._readCSVFile()

    def _readCSVFile(self):
        with open(self.filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            """Parse Data(overview, screen, action, label)"""
            for row in csv_reader:
                data = {}
                data[ClickEventCSVReader.overViewColumnName] = row[ClickEventCSVReader.overViewColumnName]
                data[ClickEventCSVReader.screenColumnName] = row[ClickEventCSVReader.screenColumnName]
                data[ClickEventCSVReader.actionColumnName] = row[ClickEventCSVReader.actionColumnName]
                data[ClickEventCSVReader.labelColumnName] = row[ClickEventCSVReader.labelColumnName]
                data[ClickEventCSVReader.tsEventColumnName] = row[ClickEventCSVReader.tsEventColumnName]
                self.dataSource.append(data)

        """Retrieve TS Event Name"""
        self.tsEventName = self.dataSource[1]["TS_event_name"]

    def getScreens(self):
        screens = CSVReader._parseScreens(self.dataSource)
        print(screens)
        return screens

    def getClickEventDict(self):
        print(self.dataSource)
        return self.dataSource

    def getTSEventName(self):
        print(self.tsEventName)
        return self.tsEventName

rd = ClickEventCSVReader('ClickEvent.csv')
rd.getScreens()
rd.getClickEventDict()
rd.getTSEventName()

