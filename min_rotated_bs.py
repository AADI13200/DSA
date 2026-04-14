def bs(a):
    n=len(a)
    low=0
    high=n-1
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2

      # to eliminate left half if it is sorted
        if a[low]<=a[mid]:
            ans=min(ans,a[low])
            low=mid+1
      # to eliminate right half if it is sorted   
        else:
            ans=min(ans,a[mid])
            high=mid-1
            
    print("minimum element in the array is : ",ans)
    
a=[4,5,6,7,0,1,2]
bs(a)
            
        
