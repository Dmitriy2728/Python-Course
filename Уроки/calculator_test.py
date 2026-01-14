
from calculator import Calculator

calculator = Calculator()

print("Start")
#res = calculator.dev(10, 0)
#assert res == None

numbers = [1,3,5,7]
res = calculator.avg(numbers)
print(res)
assert res == 4

print ("Finish")


