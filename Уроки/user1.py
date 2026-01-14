class User:
    age=10

    def __init__(self, name):
        print("Я создался")
        self.username = name
        
    def SayName(self):
        print("Меня зовут", self.username)

    def SayAge(self):
        print(self.age)

    def SetAge(self, NewAge):
        self.age=NewAge

    def addCard(self, card):
        self.card=card

    def getCard(self):
        return self.card
    