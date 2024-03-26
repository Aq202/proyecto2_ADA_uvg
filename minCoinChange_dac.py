import sys
def minCoinChange (coin, m, K):
    if K == 0:
        return 0
    minCount = sys.maxsize
    for i in range (m) :
        if coin[i] <= K:
            tempResult = 1 + minCoinChange (coin, m, K - coin[i])
            if tempResult < minCount:
                minCount = tempResult
    
    if minCount == sys.maxsize:
        return -1
    return minCount
    

print(minCoinChange([1,5,10], 3, 30))