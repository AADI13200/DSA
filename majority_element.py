# BRUTE FORCE APPROACH

'''def majority_ele(a):
    for i in a:
        count=0
        for j in a:
            if i==j:
                count+=1

    if count>len(a)//2:
       print(i, "is the majority element and occured ", count, " times")



a=[3,3,4,2,4,4,2,4,4]
majority_ele(a)'''


# OPTIMIZED APPROACH
'''def majority_ele(a):
    count=0
    ele=0
    for i in a:
        if count==0:
            count=1
            ele=i
        elif ele==i:
            count+=1
        else:
            count-=1    

    cnt1 = a.count(ele)       #Checking if the stored element is the majority element

    if cnt1>len(a)//2:
       print(ele, "is the majority element and occured ", cnt1, " times")

a=[3,3,4,2,4,4,2,4,4]
majority_ele(a)'''


# LeetCode Approach
class Solution(object):
    def majorityElement(self, nums):
        # Phase 1: Find the candidate
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Phase 2: Verify the candidate
        cnt = sum(1 for num in nums if num == candidate)
        
        if cnt > len(nums) // 2:
            return candidate
