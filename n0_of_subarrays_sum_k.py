def count_sub(a):
    cnt=0
    k=int(input("Enter the value of k: "))
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            if sum(a[i:j])==k:
                cnt+=1
                print(a[i:j])
    
    print(cnt)



a=[1,2,3,4,-1,5,6,-3,-2,-4]
count_sub(a)
#O(n^3) time complexity due to sum()

# optimized solution using hashmap
class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count