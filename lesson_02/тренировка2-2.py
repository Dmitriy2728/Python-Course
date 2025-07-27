import math

def min_boxes(x):
    return math.ceil(x/5)

num_items = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(num_items)}")
