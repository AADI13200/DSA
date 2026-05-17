'''a=[1,2,5,9,10,33]
def smallest_divisor_thresh(nums, threshold):
    for i in range(1,max(nums)+1):
        sum=0
        for j in nums:
            sum+=j//i+(j%i>0)
        if sum<=threshold:
            return i    
print(smallest_divisor_thresh(a,6))'''


# using BS brute force
def solver(a,div):
    return sum((x+div-1)//div for x in a)

def smallest_divisor_thresh(nums, threshold):
    low,high=1,max(nums)
    while low<high:
        mid=(low+high)//2
        if solver(nums,mid)<=threshold:
            high=mid
        else:
            low=mid+1
    return low
a=[1,2,3,4,5]
print(smallest_divisor_thresh(a,8))

