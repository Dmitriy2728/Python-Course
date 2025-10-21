from user1 import User
from card import Card
dima = User("Dima")

dima.SayName()
dima.SayAge()



card=Card("132 213 123", "11/26", "Dima P")
dima.addCard(card)
dima.getCard().pay(100)
