import os
import csv

class fileReader:
    def __init__(self, filename):
        self.filename=""
        self.changeFile(filename)

    def changeFile(self, filename):
        self.filename = filename
        # Check if file exists
        if os.path.exists(filename):
            print("File exists")
        else:
            print("File does not exist")
            with open(filename, mode='w') as file:
                pass  # Just to create an empty file without writing anything

    def readData(self):
        with open(self.filename, mode='r') as file:
            data = []
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
            return data
        
    def writeData2NewFile(self, filename, data):
        # Check if file exists
        if os.path.exists(filename):
            print("File already exists, please choose a new file name")
        else:
            self.writeData(filename, 'w', data)
    
    def writeData2ExistingFile(self, data):
        # Check if file exists
        if os.path.exists(self.filename):
            self.writeData(self.filename, 'a', data)
        else:
            self.writeData2NewFile(self.filename, data)

    def writeData(self, filename, mode, data):
        if(data != None and len(data) > 0):
            with open(filename, mode=mode, newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)