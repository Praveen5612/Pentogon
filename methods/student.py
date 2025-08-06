class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
s1 = Student("Praveen", 20, "A")
s2 = Student("Reddy", 22, "B")
print(s1.name, s1.age, s1.grade)
print(s2.name, s2.age, s2.grade)