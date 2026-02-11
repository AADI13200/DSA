# BRUTE FORCE APPROACH

def longest_array(a):
    sub_sum=0
    temp=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            for k in range(i,j+1):
                sub_sum+=a[k]
            if sub_sum==6:
                temp=max(temp,j-i+1)       # if i is at 2nd position and j is at 4th position then the 
                                           #length of the array will be 4-2+1=3
            sub_sum=0
    print("The longest array with sum 6 is : ",temp)    

a=[1,2,3,3,4,7,5,0]
longest_array(a)
# time complexity will be around O(n^3) because of the three nested loops and space 
# complexity will be O(1) because we are using only constant space for the variables

# OPTIMAL APPROACH

def longestSubarray(nums, k):
        n = len(nums)
        
        # To store the maximum length of the subarray
        maxLen = 0
        
        # Pointers to mark the start and end of window
        left = 0
        right = 0
        
        # To store the sum of elements in the window
        sum = nums[0]
        
        # Traverse all the elements
        while right < n:
            
            # If the sum exceeds K, shrink the window
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            
            # Store the maximum length
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += nums[right]
        
        return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15
print("The longest subarray with sum 15 is : ",longestSubarray(nums, k))
# time complexity will be around O(n) because we are traversing the array only once and 
# space complexity will be O(1) because we are using only constant space for the variables