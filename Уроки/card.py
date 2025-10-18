class Card:
        number="000 000 000"
        validDate = "12/26"
        holder = "unknown"
    
        def __init__ (self, number, date, holder):
            self.holder=holder
            self.number=number
            self.validDate=date

        def pay(self, amount):
            print("С карты", self.number, "списали", amount )

            
