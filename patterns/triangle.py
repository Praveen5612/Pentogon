# n = int(input("Enter the number : "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

# This code prints a right-angled triangle pattern using asterisks.

# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# This code prints an inverted right-angled triangle pattern using asterisks.

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
    
#     print(' '*(n-i), end =' ')
#     print('*'*i, end=' ')
#     print()

# This code prints a right-angled triangle pattern with spaces before the asterisks.

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# This code prints a right-angled triangle pattern with numbers.

# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
# This code prints an inverted right-angled triangle pattern with numbers.

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end=' ')
#     print()
# This code prints a right-angled triangle pattern with the row number repeated in each row.


# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(n, end=' ')
#     print()
# This code prints a right-angled triangle pattern with the maximum number repeated in each row.

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(n-i+1, end=' ')
    print()