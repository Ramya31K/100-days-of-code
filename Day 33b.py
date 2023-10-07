def is_palindrome(number):
    num_str = str(number)
    reversed_str = num_str[::-1]
    return num_str == reversed_str
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
