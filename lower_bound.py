# brute force approach

'''def lowerbound(a,x):
    for i in range(len(a)):
        if a[i]>=x:
            print(i)
            break

a=[3, 5, 8, 15, 19]
x=9

y=lowerbound(a,x)'''


# optimal approach

def lowerbnd(a,y):
    low,high=0,len(a)-1
    ans=len(a)

    while low <= high:
        mid=(low+high)//2
        if a[mid]>=y:
            ans=mid
            high=mid-1

        else:
            low=mid+1

    print(ans)

a=[3, 5, 8, 15, 19]
y=9
c=lowerbnd(a,y)

#Lower Bound: This is the index of the first element that is not less than the target value.
#Upper Bound: This is the index of the first element that is strictly greater than the target value.
