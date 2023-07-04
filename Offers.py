def comp_offers(A, B):
    valuation_1 = A / 0.1 
    valuation_2 = B / 0.2 
    if valuation_1 > valuation_2:
        return "Devendra should accept the first investor's offer"
    elif valuation_1 < valuation_2:
        return "Devendra should accept the second investor's offer"
    else:
        return "Both offers have the same valuation. Devendra can choose either offer."
A = int(input("enter the amount offered by the first investor:"))
B = int (input("enter the amount offered by the second investor:"))
result = comp_offers(A, B)
print(result)
