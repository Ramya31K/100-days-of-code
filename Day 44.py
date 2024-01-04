user_input = input("Enter the array elements separated by spaces: ")
arr = [int(x) for x in user_input.split()]
max_element = arr[0]
for element in arr:
    if element > max_element:
        max_element = element
print("Largest element in the array:", max_element)
