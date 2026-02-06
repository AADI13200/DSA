def left_rotate(a):
    temp=a[0]
    for i in range(len(a)):
        if a[i]==a[len(a)-1]:
            a[i]=temp
        else:
            a[i]=a[i+1]

a=[1,2,3,4,5]
print("The array before left rotation is:",a)
left_rotate(a)
print("The array after left rotation is:",a)