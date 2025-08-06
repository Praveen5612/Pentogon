n = int(input("Enter the Number : "))
count = 0
temp = n
while(n!=0):
    r = n % 10
    n = n // 10
    count += 1
n = temp
add1 = 0
while(temp!=0):
    r = temp % 10
    temp = temp // 10
    add1 = add1 + (r**count)

print('count : ',count)
print('sum : ',add1)

if(add1 == n):
    print('The number is Armstrong')
else:
    print('The number is not Armstrong')
