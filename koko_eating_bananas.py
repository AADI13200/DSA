import math

def calculatetotalhrs(piles,speed):
    totalh=0
    for bananas in piles:
        totalh+=math.ceil(bananas/speed)
    return totalh

# Function to find minimum eating speed
def minEatingSpeed(piles, h):
    # Find maximum element
    maxPile = max(piles)

    # Initialize low and high pointers
    low, high = 1, maxPile
    ans = maxPile

        # Binary search on answer space
    while low <= high:
        mid = (low + high) // 2
        totalH = calculatetotalhrs(piles, mid)

            # If possible, try smaller speed
        if totalH <= h:
            ans = mid
            high = mid - 1
            # Otherwise, try larger speed
        else:
            low = mid + 1

        return ans

# Driver code
piles = [3,4,6,7,11]
h = 8
print(minEatingSpeed(piles, h))
