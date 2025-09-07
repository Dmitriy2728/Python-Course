x=int(input("Введите номер месяца:"))

def month_to_season(x):
    if x == 1 or x == 2 or x == 12:
        print ("Зима")
    elif x == 3 or x==4 or x==5:
        print("Весна")
    elif x == 6 or x ==7 or x ==8:
        print ("Лето")
    elif x == 9 or x == 10 or x ==11:
        print("Осень")
    else:
        print ("Неверный номер месяца")

month_to_season(x)