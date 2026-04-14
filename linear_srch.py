def linear_srch(a,trget):
    for i in range(len(a)):
        if a[i]==target:
            print("Element found at index : ",i)
            break

a=[1,2,3,4,5,6,7,8,9,10]
target=int(input("Enter the element to be searched : "))
print("The array is:",a)
linear_srch(a,target)