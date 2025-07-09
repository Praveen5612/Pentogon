def max_finder(arr):
    """Function to find the maximum number in a list."""
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Validate input length
if len(arr) != n:
    print(f"Error: Expected {n} elements, but got {len(arr)}")
else:
    print("The maximum number is:", max_finder(arr))
