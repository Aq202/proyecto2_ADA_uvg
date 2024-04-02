'''
Análisis y Diseño de Algoritmos - Sección 20
Proyecto 2
Minimum Coin Change Problem - Programación Dinámica

Autores: Diego Aquino y Pablo Zamora
'''

import time
import sys
def minCoinChange (coin, m, K):
    if K == 0:
        return 0
    change = [sys.maxsize] * (K + 1)
    change[0] = 0
    for i in range(1, K + 1) :
        for j in range(m):
            if coin[j] <= i:
                currentCount = 1 + change[i - coin[j]]
                if currentCount < change[i]:
                    change[i] = currentCount
    
    if change[K] == sys.maxsize:
        return -1
    return change[K]
    
start_time = time.time()

minCoinChange([1,5,10,15,20,25,30,35,40,45,50,55,60,65,70], 15, 175)

print(f"{(time.time() - start_time)}")