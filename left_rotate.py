def rotate(a):
    temp=a[0]
    for i in range(len(a)):
        if i==len(a)-1:
            a[i]=temp
        else:
            a[i]=a[i+1]

a=[1,2,3,4,5]
print("Array before rotation is : ",a)
rotate(a)
print("Array after rotation is : ",a)