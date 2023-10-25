#deci to binary 

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
if __name__ == '__main__':
    dec_val = int(input("enter a number:"))
    DecimalToBinary(dec_val)

#binary to deci

b_num = list(input("Input a binary number: "))
value = 0
for i in range(len(b_num)):
     digit = b_num.pop()
if digit == '1':
     value = value + pow(2, i)
print("The decimal value of the number is", value)
