def quicksort(arr):

    if len(arr) <= 1:

        return arr

    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)

user_input = input("Enter the array elements: ")

arr = [int(x) for x in user_input.split()]

sorted_arr = quicksort(arr)

print("Sorted array:", sorted_arr)
 
