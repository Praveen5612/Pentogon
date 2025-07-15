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

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(n-i+1, end=' ')
#   print()

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i+j-1, end=' ')
#     print()

# This code prints a right-angled triangle pattern with the sum of the row and column indices in each cell.

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i*j, end=' ')
#     print()
# This code prints a right-angled triangle pattern with the product of the row and column indices in each cell.


# n = int(input('Enter a number: '))
# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=' ')
#         num += 1
#     print()
# This code prints a right-angled triangle pattern with consecutive numbers starting from 1 in each row.

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if (i + j) % 2 == 0:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# This code prints a right-angled triangle pattern with alternating asterisks and spaces based on the sum of the row and column indices.
# The asterisk is printed if the sum of the row and column indices is even, otherwise

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(64+j), end=' ')
#     print()
# a space is printed.
# This code prints a right-angled triangle pattern with letters starting from 'A' in each

# n = int(input('Enter a number: '))
# for i in range(n):
#     for j in range(n):
#         if i ==0 or j==0 or i == n-1 or j == n-1:
#             print('*', end = ' ')
#         elif i== j or i+j == n-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')

#     print()
# This code prints a square pattern with asterisks on the borders and spaces inside.

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(' ' * (n - i) + '*' * (i*2-1))

# This code prints a right-angled triangle pattern with asterisks aligned to the right.

# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))
# This code prints an inverted right-angled triangle pattern with asterisks aligned to the right.

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(' '*(n-i) + '*' * (2*i -1))
for j in range(n-1, 0, -1):
    print(' ' * (n - j) + '*' * (2 * j - 1))
# This code prints a pyramid pattern with asterisks, where each row has an increasing number of asterisks centered in the output.
# The first loop prints the upper half of the pyramid, and the second loop prints the lower half of the pyramid in reverse order.
# The number of asterisks in each row is determined by the current row index, and spaces are added to center the asterisks in each row.
# The output will form a complete pyramid shape with asterisks.