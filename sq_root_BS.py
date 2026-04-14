# brute force method to find the square root of a number
'''def findsq(a):
    n=int(input("Enter the number: "))
    ans=1
    for i in range(1,n+1):
        if i*i <= n:
            ans=i
        else:   
            break
    print("The square root of the number is: ",ans)


a=[5,10,15,20,25]
for i in a:
    findsq(i)'''


#optimized method to find the square root of a number using binary search
def findsq(a):
    n=int(input("Enter the number : "))
    low,high=1,n
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid <= n:
            ans=mid
            low=mid+1
        else:
            high=mid-1  
    print("The square root of the number is: ",ans)

a=[5,10,15,20,25]
for i in a:   
    findsq(i) 