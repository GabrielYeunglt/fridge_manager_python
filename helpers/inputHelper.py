from datetime import datetime


class inputHelper:
    def getFloatInput(inputName):
        result = 0
        inputValid = False
        while not inputValid:
            msg = "Please input " + inputName + " "
            inputStr = input(msg)
            try:
                result = float(inputStr)
                inputValid = True
            except ValueError:
                print("Please input numeric value")
        return result

    def getDateInput(inputName):
        date = datetime.now()
        dateStr = ""
        dateValid = False
        while not dateValid:
            try:
                msg = "Please enter the " + inputName + " (YYYY-MM-DD or empty as current date): "
                dateStr = input(msg)
                if dateStr == None or dateStr == "":
                    date = datetime.now()
                else:
                    # Parse the date string
                    date = datetime.strptime(dateStr, "%Y-%m-%d")
                dateValid = True
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return date

    def getBooleanInput(inputName):
        msg = "Please enter " + inputName + " (Y/N) "
        tf = input(msg)
        return tf == "y" or tf == "Y"

    def getStringInput(inputName):
        msg = "Please enter " + inputName + " "
        return input(msg)
