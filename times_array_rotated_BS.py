def bs(a):
    n=len(a)
    low=0
    high=n-1
    ans=float('inf')
    index=-1
    
    while low<=high:
        mid=(low+high)//2
        
        if a[low]<=a[high]:
            if a[low]<ans:
                index=low
                ans=a[low]
            break
                
        if a[low]<=a[mid]:
            if a[low]<ans:
                index=low
                ans=a[low]
            low=mid+1
            
        else:
            high=mid-1
            if a[mid]<=ans:
                index=mid
                ans=a[mid]
            
    print("The array is rotated",index,"times")
    
a=[4,5,6,7,0,1,2]
bs(a)
            
        
