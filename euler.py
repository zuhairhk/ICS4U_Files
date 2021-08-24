def euler(n):
    totalTerms = 1

    print()
    print('-------------')
    print('For #:', n)
    print('-------------')
    print()
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        elif n % 2 != 0:
            n = int((n * 3)) + 1
        
        print('num is:', n)

        totalTerms += 1
    
    print('Total Terms:', totalTerms)
    return totalTerms

# print(euler(13))
mill = 100
chain = [0] * mill
maxChain = 0

for i in range(1, mill + 1):
    chain[i-1] = euler(i)
    if chain[i-1] >= maxChain:
        maxChain = chain[i-1]

print('Max Chain is:', maxChain)