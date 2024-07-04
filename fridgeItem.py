from datetime import datetime, timedelta

class fridgeItem:
    def __init__(self, name = None, qty = 0, unit = None, createDate = datetime.now, expiryAfter = 7, exist = True):
        self.name = name
        self.qty = qty
        self.unit = unit
        self.createDate = createDate
        dayToExpire = timedelta(days=expiryAfter)
        self.expiryDate = self.createDate + dayToExpire
        self.exist = exist
        pass