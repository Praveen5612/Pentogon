def maxOfTwo(arr):
    max_num_2 = arr[0]
    unique_elements = list(set(arr))
    unique_elements.sort()
    print("Unique elements:", unique_elements)
    
    if len(unique_elements) > 1:
        max_num_2 = unique_elements[1]
    return max_num_2


n = int(input("Enter the number of elements: "))
arr = list(map(int,input("Enter the elements separated by space: ").split()))

if len(arr) != n:
    print(f"Error: Expected {n} elements, but got {len(arr)}")
else:
    print("The maximum number is:", maxOfTwo(arr))