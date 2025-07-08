a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input('Enter the third value: '))

if a>b & a>c:
    print("A is the bigger number: ", a)
elif b>a & b>c: 
    print("B is greater number: ", b)
elif c>a & c>b:
    print('c is grater number: ', c)
elif a==b & b==c:
    print('all values are equal',a,b,c)
