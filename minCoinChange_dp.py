import sys
'''
Análisis y Diseño de Algoritmos - Sección 20
Proyecto 2
Minimum Coin Change Problem - Programación Dinámica

Autores: Diego Aquino y Pablo Zamora
'''

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
    

print(minCoinChange([1,5,10], 3, 30))