a=[4,5,7,8,5,43,23,9,8,77,50,88]

largest=a[0]

for i in range(0,len(a)):
    if (a[i]>largest):
        largest=a[i]
print(a[i]," is largest among all")


#else we can sort the array and last element is the largest among all
#print(a[-1]) will give the last element from the sorted array 

