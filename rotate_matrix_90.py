#  OPTIMIZED APPROACH (just space optimized)
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


# BRUTE FORCE APPROACH(using extra space than optimized approach)
class Solution:
    # Function to rotate the matrix 90 degrees clockwise using extra space
    def rotateClockwise(self, matrix):
        # Get the size of the square matrix
        n = len(matrix)

        # Create a new matrix of same size to store rotated result
        rotated = [[0] * n for _ in range(n)]

        # Traverse each element of original matrix
        for i in range(n):
            for j in range(n):
                # Place the element at its new rotated position
                rotated[j][n - i - 1] = matrix[i][j]

        # Return the rotated matrix
        return rotated

# Driver code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
rotated = obj.rotateClockwise(matrix)

# Print the rotated matrix
for row in rotated:
    print(*row)


#both the codes have same time complexity of O(n^2) but the optimized approach 
# uses extra space of O(n^2) while the brute force approach does it in place with O(1) extra space.
