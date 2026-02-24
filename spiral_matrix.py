def spiral_matrix(a):
    n=len(a)
    top=0
    bottom=n-1
    left=0
    right=n-1

    for i in range(left, right+1):
        print(a[top][i], end=" ")
    top+=1
    for i in range(top, bottom+1):
        print(a[i][right], end=" ")
    right-=1
    for i in range(right, left-1, -1):
        print(a[bottom][i], end=" ")    
    bottom-=1
    for i in range(bottom, top-1, -1):
        print(a[i][left], end=" ")
    left+=1

# Driver code
a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]         
spiral_matrix(a)
#one and only code