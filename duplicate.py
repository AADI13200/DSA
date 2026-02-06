def duplicate(a):
    i=0
    for j in range(1,len(a)):
        # bascially taking i to check whether it is equal to j or not, 
        # if it is not equal then we will increment i and assign the value of a[j] to a[i]
        if a[i]!=a[j]:
            i+=1
            a[i]=a[j]
            
    # i is last index of unique element, count = i + 1
    return a[:i+1]


a=[1,1,2,3,4,5,5,6,7,8,9,9]
s=duplicate(a)
print("The array before removing duplicates is:",a)
print("The array after removing duplicates is:",s)