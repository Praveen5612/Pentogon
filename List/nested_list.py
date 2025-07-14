# # rows = int(input("Enter the number of rows: "))
# # nested_list = []
# # for i in range(rows):
# #     l1 = list(map(int,input().split()))
# #     nested_list.append(l1)
# # print("The nested list is:", nested_list)



# if __name__ == '__main__':
#     nested_list = []
#     n = int(input("Enter the number of entries: "))
#     for _ in range(n):
        
        
#         entry = input().split()
        
#         name = entry[0]
#         score = int(entry[1])
#         name = entry[0]
#         score = int(entry[1])
        
#         nested_list.append([name,score])
        
        
#     print(nested_list)

#     nested_list.sort(key=lambda x: (x[1], x[0]))
#     print("Sorted nested list:", nested_list)





if __name__ == '__main__':
    nested_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    # Step 1: Get all unique scores in sorted order
    scores = sorted(set(score for name, score in nested_list))

    # Step 2: Get the second lowest score
    second_lowest = scores[1]

    # Step 3: Get all names with that score
    names = [name for name, score in nested_list if score == second_lowest]

    # Step 4: Sort names alphabetically and print
    names.sort()
    for name in names:
        print(name)


