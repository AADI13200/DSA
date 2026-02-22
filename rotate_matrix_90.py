# BRUTE FORCE APPRAOCH
def rotate_matrix(a):
    n = len(a)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap a[i][j] with a[j][i]
            a[i][j], a[j][i] = a[j][i], a[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        a[i].reverse()

# Driver code
a = [[1, 2, 3],
     [4, 5, 6], 
     [7, 8, 9]]

rotate_matrix(a)

for row in a:
    print(row)