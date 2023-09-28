#abcd pattern 
class Solution:
    def printTriangle(self, N):
        ascii_val = 65
        for i in range(1, N + 1):
            string = ""
            for j in range(ascii_val, ascii_val + i):
                string = string + chr(j)
            print(string)

#number pattern
n= int(input("Enter the number of rows: "))

number = 1
for i in range(1, n + 1):
    for j in range(i):
        print(number, end=' ')
        number += 1
    print()
