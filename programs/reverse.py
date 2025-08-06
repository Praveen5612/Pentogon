# n = int(input('Enter the number : '))
# rev = 0
# while(n!=0):
#     r = n%10
#     n = n//10
#     rev = rev*10
#     rev = rev+r
# print(r, ' ')
# print(rev)

string = input('Enter the string : ')
rev_string = ''
for char in string:
    rev_string = char + rev_string
print(rev_string)