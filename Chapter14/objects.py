#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class DailySales:
    amount:float = 0.0
    month:int= 0
    day:int = 0
    year:int = 0
    quarter:int = 0

    @property
    def hasBadAmount(self):
        if self.amount == "?":
            return True
        else:
            return False
        
    @property
    def hasBadMonth(self):
        if self.month == "?":
            return True
        else:
            return False
        
    @property
    def hasBadDay(self):
        if self.day == "?":
            return True
        else:
            return False
    
    @property
    def hasBadYear(self):
        if self.year == "?":
            return True
        else:
            return False
        
    @property
    def hasBadData(self):
        if self.hasBadAmount or self.hasBadMonth or self.hasBadDay or self.hasBadYear:
            return True
        else:
            return False

    def fromFile(self,row):
        # Amount
        try:
            self.amount = float(row[[0]])
        except ValueError:
            self.amount = "?"
        # Quarter
        self.setQuarter()
    
    def toList(self):
        if self.hasBadData:
            return None
        else:
            return [self.amount,self.month,self.day,self.year,self.quarter]

    def setQuarter(self):
        if self.hasBadMonth:
            self.quarter = 0
        else:
            if self.month >=1 and self.month <= 3:
                self.quarter = 1
            elif self.month >= 4 and self.month <=6:
                self.quarter = 2
            elif self.month >= 7 and self.month <=9:
                self.quarter = 3
            elif self.month >= 10 and self.month <=12:
                self.quarter = 4       

class SalesList:
    def __init__(self):
        self.__sales = []
        self.hasBadData = False

    @property
    def count(self):
        return len(self.__sales)

    def get(self, index):
        if index >= self.count:
            return None
        else:
            return self.__sales[index]

    def add(self, data):
        self.__sales.append(data)

    def concat(self, sales_list):
        for i in range(sales_list.count):
            self.add(sales_list.get(i))

def main():
    pass

# if started as the main module, call the main function
if __name__ == "__main__":
    main()