n=int(input("Enter the number of elements : "))
a=[]
for i in range(n):
    e=int(input("Enter the elements in the array : "))
    a.append(e)

# main computation

for i in range(1,n):
    key=a[i]
    j=i-1

    while(j>=0 and a[j]>key):
        # swapping but in different way
        a[j+1]=a[j]
        j-=1

    a[j+1]=key

print(a)
        # 9 5 4 5 1 3 6 4 3 8 
        # j i