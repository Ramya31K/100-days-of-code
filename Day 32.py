class Solution:
    def printTriangle(self, n): 
        for i in range(1, 2*n): 
            for j in range(1, 2*n):
                row, col = i, j
                if row > n:
                    row = 2 * n - row
                if col > n:
                    col = 2 * n - col
                print(n - min(row, col) + 1, end = ' ')
            print()
    printTriangle(1,4)
  
