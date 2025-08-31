n=int(input("Введите число n:"))

def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 15 == 0: 
            print("fizz_buzz")
        elif x % 5 == 0:
            print("buzz")
        elif x % 3 == 0:
            print ("fizz")
        else: 
            print(x)

fizz_buzz(n)




