#Brute Force Approach

def leader(a):
    ans=[]
    for i in range(len(a)):
        leader=True
        for j in range(i+1,len(a)):
            if a[j]>a[i]:
                leader=False
                break

        if leader:
            ans.append(a[i])
    print(ans)

a=[16,17,4,3,5,2]
leader(a)

#Optimal Approach
class Solution:
    # Function to find the leaders in an array.
    def leaders(self, nums):
        ans = []
        
        if not nums:
            return ans
        
        # Last element of the list is always a leader
        max_val = nums[-1]
        ans.append(nums[-1])
        
        # Check elements from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_val:
                ans.append(nums[i])
                max_val = nums[i]
        
        '''Reverse the list to match
        the required output order'''
        ans.reverse()
        
        # Return the leaders
        return ans

# Main method
nums = [10, 22, 12, 3, 0, 6]

# Create an instance of the Solution class
finder = Solution()

# Get leaders using class method
ans = finder.leaders(nums)

print("Leaders in the array are: ", end="")
for leader in ans:
    print(leader, end=" ")
print()