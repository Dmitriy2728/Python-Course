from student import Student
from coursegroup import CourseGroup

student=Student("Дима", "Палкин", "34", "Тестировщик")
classmate1=Student("Вася", "Иванов", "35", "Тестировщик")
classmate2=Student("Миша", "Петров", "20", "Тестировщик")
classmate3=Student("Женя", "Сидоров", "36", "Тестировщик")

testers=CourseGroup(student, [classmate1,classmate2, classmate3])

print(testers)