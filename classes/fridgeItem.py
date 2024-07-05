from datetime import datetime, timedelta


class fridgeItem:
    def __init__(self, name=None, qty=0, unit=None, createDate=datetime.now, expiryAfter=7, exist=True):
        self.name = name
        self.qty = qty
        self.unit = unit
        self.createDate = createDate
        dayToExpire = timedelta(days=expiryAfter)
        self.expiryDate = self.createDate + dayToExpire
        self.exist = exist
        pass

    def initFromData(self, data):
        if (data != None and len(data) > 0):
            return fridgeItem(data[0], data[1], data[2], data[3], data[4], data[5])
