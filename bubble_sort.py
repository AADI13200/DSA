n=int(input("Enter the number of elements in the array : "))
a=[]
for i in range (n):
    e=int(input("Enter the elements in the array : "))
    a.append(e)
for i in range(n):
    for j in range(i+1,n):
        if (a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("sorted array is : ",a)