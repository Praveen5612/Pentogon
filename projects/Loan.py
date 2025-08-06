# class farmer:
#     ROI = 2.5
#     def __init__(self, principle,time):
#         self.principle = principle
#         self.time = time
#     def loan(self):
#         Simple_Interest = (self.principle * farmer.ROI * self.time) / 100
#         print('Simple Interest is:', Simple_Interest)
# f1 = farmer(300000, 0.5)  # Assuming time is in years
# f1.loan()



class Demo:
    def display(self,a=10,b=20,c=30):
        print('a:', a)
        print('b:', b)
        print('c:', c)
d = Demo()
x=11
y=22
z=33
d.display()  # Using default values
d.display(x, y, z)  # Passing all three arguments
d.display(a=z,b=x,c=y)  # Passing two arguments, using default for c