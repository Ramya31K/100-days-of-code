def qualify(A, B, X):
    total_score = A + 2*B
    if total_score >= X:
        return "Chef qualifies for the next round!"
    else:
        return "Chef does not qualify for the next round."
A = int(input("Enter the number of easy problems solved: "))
B = int(input("Enter the number of hard problems solved: "))
X = int(input("Enter the minimum required score: "))
result = qualify(A, B, X)
print(result)
