# BRUTE FORCE APPROACH

def appear_once(a):
    for i in range(0,len(a)):
        count=0
        temp=a[i]
        for j in range(0,len(a)):        # O(n^2) time complexity
            if temp==a[j]:
                count+=1
        if count==1:
            print(temp," appears once in the array")
            break
        
a=[1,2,3,4,3,2,1]
appear_once(a)


# OPTIMAL APPROACH
#refer video

