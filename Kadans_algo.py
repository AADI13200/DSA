# Kadans Algorithm is used to find the maximum sum of a contiguous subarray in an array of integers.
#BRUTE FORCE APPROACH

'''def kadans_algo(a):
    maxi = float('-inf')
    
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            total = 0
            for k in range(i,j+1):
                total += a[k]
            
            if total==7:
                print(a[i:j+1],"is the subarray with the maximum sum of 7")


a = [1,2,3,4,5,6,7,8,9]
kadans_algo(a)'''


#OPTIMIZED APPROACH
'''def kadans_algo(a):
    maxi=float('-inf')
    for i in range(len(a)):
        total=0
        for j in range(i,len(a)):
            total+=a[j]
            if total==7:
                print(a[i:j+1],"is the subarray with the maximum sum of 7")

a = [1,2,3,4,5,6,7,8,9]
kadans_algo(a)'''

# Actual Kadans Algorithm


def max_subarray_sum(arr):
    current_sum = 0
    maximum = float('-inf')  # Equivalent to LONG_MIN
    
    for num in arr:
        current_sum += num
        
        if current_sum > maximum:
            maximum = current_sum
        
        if current_sum < 0:
            current_sum = 0
            
    return maximum
arr = [1, 2, 3, -2, 5]
print(max_subarray_sum(arr))  # Output: 9

#explnation:
#1st element → 1
#current_sum = 0 + 1 = 1
#maximum = max(-∞, 1) = 1

#2nd element → 2
#current_sum = 1 + 2 = 3
#maximum = max(1, 3) = 3

#3rd element → 3
#current_sum = 3 + 3 = 6
#maximum = max(3, 6) = 6

#4th element → -2
#current_sum = 6 + (-2) = 4
#maximum = max(6, 4) = 6


#(Sum is still positive, so we continue)

#5th element → 5
#current_sum = 4 + 5 = 9
#maximum = max(6, 9) = 9(final answer)