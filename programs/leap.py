year = int(input('Enter the number : '))
if year%4 == 0 and year%100 != 0:
    print('Leap Year')
else:
    print('Not a Leap Year')