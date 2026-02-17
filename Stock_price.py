def stock_prices(a):
    max_profit,profit=0,0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            profit=a[j]-a[i]

            max_profit=max(max_profit,profit)
    return max_profit

a=[7,1,5,3,6,4] 
print(stock_prices(a))

#i = 0 (Buy at 7)
#j = 1 → 1 - 7 = -6
#j = 2 → 5 - 7 = -2
#j = 3 → 3 - 7 = -4
#j = 4 → 6 - 7 = -1
#j = 5 → 4 - 7 = -3
#Max profit still = 0

#i = 1 (Buy at 1)
#j = 2 → 5 - 1 = 4 ✅
#j = 3 → 3 - 1 = 2
#j = 4 → 6 - 1 = 5 ✅ (New max)
#j = 5 → 4 - 1 = 3
#Max profit becomes 5


#Brute Force Approach 
class Solution:
    # Function to calculate maximum profit using single pass
    def stockbuySell(self, prices):
        # Initialize the minimum price to a large number
        min_price = float('inf')

        # Initialize the maximum profit to 0
        max_profit = 0

        # Traverse each price in the array
        for price in prices:
            # If current price is less than min_price, update min_price
            if price < min_price:
                min_price = price
            # Else calculate profit and update max_profit if it's greater
            else:
                max_profit = max(max_profit, price - min_price)

        # Return the maximum profit found
        return max_profit

# Driver code
obj = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(obj.stockbuySell(prices))
    