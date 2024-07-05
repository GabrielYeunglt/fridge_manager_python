from classes.fridgeItem import fridgeItem
from helpers.fileReader import fileReader
from helpers.inputHelper import inputHelper
from datetime import datetime


def main():
    print("Welcome to fridge manager!")

    userInput = 99
    rawData = []
    data = []

    fr = fileReader("data.csv")
    rawData = fr.readData()

    if rawData != None and len(rawData) > 0:
        for rd in rawData:
            data.append(fridgeItem(rd))

    while (userInput != 0):
        print("1: Show existing records")
        print("2: Add item")
        print("3: Delete item")
        tempInput = input("Please select your operation: ")
        try:
            userInput = int(tempInput)
            # show data
            if (userInput == 1):
                print("=== Show Item ===")
                print()
                for dt in data:
                    print(dt)
            # add data
            elif (userInput == 2):
                print("=== Add Item ===")
                print()
                name = inputHelper.getStringInput("item name")
                qty = inputHelper.getFloatInput("quantity")
                unit = inputHelper.getStringInput("unit")
                date = inputHelper.getDateInput("create date")
                expiryAfter = inputHelper.getFloatInput("number of days to expiry")
                exists = inputHelper.getBooleanInput("existence")
                newItem = fridgeItem(name, qty, unit, date, expiryAfter, exists)
                data.append(newItem)
                pass

        except ValueError:
            print("Operation not found!")


main()
