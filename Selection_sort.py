n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range (n):
    e=int(input("enter the elements in the array : "))
    arr.append(e)

for i in range(n):
    for j in range(i+1,n):
        if (arr[i]>arr[j]): 
            # swapping
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("sorted array is : ",arr)