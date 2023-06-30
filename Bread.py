def bread(N, M, K):
    total_days = N / K

    if total_days <= M:
        return "Yes, Eikooc can eat all the loaves before they expire."
    else:
        return "No, Eikooc cannot eat all the loaves before they expire."
N = int(input("enter n value : "))
M = int(input("enter m value : "))
K = int(input("enter k value : "))
result = bread(N, M, K)
print(result)
