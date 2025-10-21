from student import Student
class CourseGroup:
    def __init__(self, student, classmate):
        self.student=student
        self.classmate=classmate

    def __str__(self):
        classmate_str = ", ".join([str(classmate) for classmate in self.classmate])
        return f"{self.student} учится вместе с: {classmate_str}"