n = int(input('Enter the number : '))
a = 0
b = 1
for i in range(1,n+1):
    c = a+b
    print(a,end = ' ')
    a = c-a
    a = b
    b = c
    
