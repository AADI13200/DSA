# BRUTE FORCE APPROACH (O(n^2))
'''def check_srt(arr,n):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]>a[j]):
                return False
    return True

a=[1,5,3,2,4]
n=len(a)

ans=check_srt(a,n)

if ans:
    print("Array is sorted !")

else:
    print("Array is not sorted !")'''


# OPTIMAL APPROACH (O(n))

def check_sort(a,n):
    for i in range(1,n):
        if (a[i]<a[i-1]):
            return False
    return True

a=[1,2,3,4,5]
n=len(a)

ans=check_sort(a,n)

print("array is sorted" if ans else "Array is not sorted")