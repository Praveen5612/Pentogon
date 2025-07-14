# n = int(input("Enter the number of elements in the list: "))
# elements = []
# for i in range(n):
#     element = int(input("Enter element {}: ".format(i + 1)))
#     elements.append(element)
# print("The list is:", elements)


# ele = int(input('Enter the number of elements in the list: '))
# elements = []
# for i in range (ele):
#     val = int(input(f'Enter element {i + 1}: '))
#     elements.append(val)
# print("The list is:", elements)

# my_list = list(map(int, input("Enter elements separated by space: ").split()))
# print("List is:", my_list)
# my_list.insert(3, [5, 6])
# print(my_list)  # [1, 100, 2, 3, 4, 5, 6]


# l1 = list(map(int,input("Enter elements separated by space: ").split()))
# l2 = list(map(int,input("Enter elements separated by space: ").split()))
# print(l1)
# print(l2)
# l1.extend(l2)
# print(l1)  
# # This will print the combined list

l1 = [x*2 for x in range(1,100,2) if x%2==0]
print(l1)  # This will print [0, 4, 8, 12, 16]