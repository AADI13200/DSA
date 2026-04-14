def binary_srch(a):
    #works on sorted array
    low = 0
    high = len(a) - 1
    n=int(input("Enter the number to be searched: "))
    while low<=high:
        mid=(low+high)//2      # to get absolute value of mid
        if a[mid]==n:
            print("Element found at index: ", mid)
            break

        elif a[mid]>n:
            high=mid-1

        else:   
            low=mid+1

    if low>high:
        print("Element not found in the array !! ")


a=[1,2,3,4,5,6,7,8,9]
binary_srch(a)
