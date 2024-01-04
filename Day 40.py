def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
user_input = input("Enter numbers : ")
numbers = [int(num) for num in user_input.split()]
bubble_sort(numbers)
print("Sorted list:", end=' ')
print(numbers)
