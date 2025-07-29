# To print number of * you want and with out space
# for i in range(1,1000):
#     print('*',end='')

# To print number of * you want and with space
# for i in range(1,5+1,1):
#     print('* ',end='')

# to print numbers
# for i in range(1,6):
#     print(i ,end=' ')

# n =1
# for i in range(1,5+1,1):
#     print(n,' ',end='')
#     n = n+1

#to print letters
# print('\n')
# for i in range(1,27):
#     print(chr( 64+i) ,end=' ')
# print('\n')
# for j in range(1,27):
#     print(chr(96+j),end = ' ')

#to print a square
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end=' ')
#     print('*')

# To print a hallow sqare 
# n= int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if((j==1) or (j==n) or (i==1) or (i==n)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
#to print numbers hallow square
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if((j==1) or (j==n) or (i==1) or (i==n)):
#             print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=' ')
#         i+=1

#     print()
# n = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end='')
#         n+=1
#     n=1
#     print()
# n=64 
# for i in range(1,5,1):
#     for j in range(1,5,1):
#         print(chr(n),end =' ')
#         n+=1
#     print()


# triangle patterns
#Right angled triangle
# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print(chr(64+i),end=' ')
#     print()


#Inverse Right angled triangle
# for i in range(1,6,1):
#     for j in range(1,(6-i)+1,1):
#         print('* ' ,end=' ')
#     print()

# reverse triange
# n=6
# for i in range(1,n,1):
#     for j in range(1,n-i,1):
#         print('  ',end ='')
#     for j in range(1,i+1,1):
#         print('* ',end='')
#     print()

#inverse reverse triangle
# n=6
# for i in range(1,n,1):
#     for j in range(1,i,1):
#         print('  ',end ='')
#     for j in range(1,n-i+1,1):
#         print('* ',end='')
#     print()

# empty square
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print('* ',end = '')
#         else:
#             print(' ',end = ' ')
#     print()

# Empty triangle
# for i in range(1,7):
#     for j in range(1,i+1):
#         if (i==1 or j==1 or i==j or i == 6 ):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

#regular diagonal
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print('*',end = '')
#         else:
#             print(' ',end = ' ')
#     print()

#cross diagonal
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j == n+1:
#             print('*',end = '')
#         else:
#             print(' ',end = ' ')
#     print()

#triangle boundary patterns
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i+j == n+1:
#             print('* ',end = '')
#         else:
#             print('  ',end = '')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==n or j==n or i+j == n+1:
#             print('* ',end = '')
#         else:
#             print('  ',end = '')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or j==1 or i==n or j ==n or i==j or i+j == n+1):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or j==1 or i==n or j ==n or i==j or i+j == n+1 or i==n//2 or j==n//2 ):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==j or i+j == n+1 or i==n//2 or j==n//2 ):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()


# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==n//2 or j==n//2 ):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

# n=11
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==j or i+j == n+1):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

# n=3
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end = ' ')
#     for j in range(1,n-i+1):
#         print('#',end = ' ')
#     for j in range(1,n-i+1+1):
#         print('#',end = ' ')
#     for j in range(1,i+1):
#         print('*',end = ' ')
#     for j in range(1,1+1,1):
#         print('*',end='')
#     print()

# n = 5
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1,1):
#         print('#',end=' ')
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     for j in range(1,n-i+1,1):
#         print('#',end=' ')
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     for j in range(1,i-1+1,1):
#         print("*",end = ' ')
#     print()




#Fusion
# n= 3
# for i in range(1,n+1):
#     for j in range(1,n-i+1,1):
#         print(' ',end=' ')
    
#     for j in range(1,i+1,1):
#         print('*',end = ' ')
#     for j in range(1,i,1):
#         print('*',end=' ')
#     print()
# n = 2
# for i in range(1,n+1,1):
#     for j in range(1, i+1,1):
#         print(' ',end = ' ')
#     for j in range(1,n-i+1,1):
#         print('*',end =' ')
#     for j in range(1,n-i+1+1,1):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1,2):
#     spaces = (n-i) //2
#     print('  '*spaces+'* '*i)
# for i in range(n-2,0,-2):
#     spaces=(n-i)//2
#     print('  '*spaces+'* '*i)




# #hallow Diamond
# n = 4
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i+j == n+1):
#             print('*', end = ' ')
#         else:
#             print(' ',end = ' ')
#     for j in range(1,n+1,1):
#         if(i==j+1):
#             print('*',end= ' ')
#         else:
#             print(' ',end = ' ')
#     print()
# n = 3
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i == j-1):
#             print('*', end = ' ')
#         else:
#             print(' ',end = ' ')
#     for j in range(1,n+1,1):
#         if(i+j == n+1):
#             print('*',end= ' ')
#         else:
#             print(' ',end = ' ')    
#     print()

#  Daimond shape
# n=4
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1+1,1):
#         print('*',end = ' ')
#     for j in range(1,i-1+1,1):
#         print('-',end = ' ')
#     for j in range(1,i-1+1,1):
#         print('-',end = ' ')
#     for j in range(1,n-i+1+1,1):
#         print('*',end = ' ')
#     print()
# n = 4
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     for j in range(1,n-i+1,1):
#         print(' ',end = ' ')
#     for j in range(1,n-i+1,1):
#         print(' ',end = ' ')
#     for j in range(1,i+1,1):
#         print('*',end = ' ')
#     print()



#CAT
n=3
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print('*',end = ' ')
    for j in range(1,n-i+1,1):
        print(' ',end = ' ')
    for j in range(1,n-i+1,1):
        print(' ',end = ' ')
    for j in range(1,i+1,1):
        print('*',end = ' ')
    print()
n=4
for i in range(1,n+1,1):
    for j in range(1,6+1,1):
        if(i==1 or i==4 or j==1 or j==6):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
n=6
for i in range(1,n+1,1):
    for j in range(1,12+1,1):
        if(i==1 or i==6 or j==1 or j==12):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,6+1,1):
        if(i==5 or i==6):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
n = 4
for i in range(1,n+1,1):
    for j in range(1,6+1,1):
        if(j==1 or j==2 or j==5 or j==6):
            print('*',end = ' ')
        else:
            print(' ',end=' ')
    print()