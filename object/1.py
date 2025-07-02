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

f1 = fan()
print(f1.brand)
print(f1.color)
print(f1.price)
print(f1.blades)

f1.on()
f1.rotate()
f1.off()


