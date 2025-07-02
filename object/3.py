class fan:
    def __init__(self):
        self.brand = " Usha "
        self.color = "Black "
        self.price = 3000
        self.blades = 3

    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is running")
    def off(self):
        print("fan is turned off")


class Student:
    def __init__(self):
        
        self.name = "Praveen"
        self.age = 22
        self.phNo = 630314167
    def play(self):
        print("Plaing Chess")


f1 = fan()
print(f1.brand)
print(f1.color)
print(f1.price)
print(f1.blades)

f1.on()
f1.rotate()
f1.off()

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.phNo)
s1.play()