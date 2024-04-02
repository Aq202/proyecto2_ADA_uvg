'''
Análisis y Diseño de Algoritmos - Sección 20
Proyecto 2
Minimum Coin Change Problem - DaC

Autores: Diego Aquino y Pablo Zamora
'''

import sys
import time
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
    
start_time = time.time()

minCoinChange([1,5,10,15,20,25], 6, 15)

print(f"{(time.time() - start_time)}")