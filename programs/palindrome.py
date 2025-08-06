n = int(input('Enter the number : '))
rev = 0
temp = n
while (n!=0):
    r = n % 10
    n = n // 10
    rev = rev *10 + r
print(rev)
if n == rev:
    print("palindrome")
else:
    print('Not Palindrome')


# string = input('Enter the string : ')
# rev_string = ''
# for i in string:
#     rev_string = i+ rev_string
# print(rev_string)
# if string == rev_string:
#     print('Palindrome')
# else:
#     print('Not Palindrome')