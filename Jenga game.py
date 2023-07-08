def game_valid(N, X):
    if X == N:
        return True
    else:
        return False
N = int(input("Enter the number of people at the party: "))
X = int(input("Enter the number of tiles available: "))
validity = game_valid(N, X)
if validity:
    print("The Jenga game is valid.")
else:
    print("The Jenga game is invalid.")
