def good_program (bits):
    nibbles = bits // 4 
    if nibbles > 0 and bits % 4 == 0:
        return "Good"
    else:
        return "Not Good"
bits=int(input("enter the number of bits:"))
result=good_program(bits)
print(result)
