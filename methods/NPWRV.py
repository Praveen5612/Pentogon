class calci:
    def __init__(self):
        self.brand = 'Casio'
        self.color = 'Black'
    def add(self):
        a = 10
        b = 20
        c = a+b
        return c
c1 = calci()
print(c1.brand)
print(c1.color)
res = c1.add()
print(res)
c1.x=10
print(c1.x)
