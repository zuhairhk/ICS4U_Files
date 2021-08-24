def nthPrime(location):
    '''
    :param location:
    :return:
    '''

    primeList = []
    startNumber = 2

    while len(primeList) != location:
        if isPrime(startNumber):
            primeList.append(startNumber)
        # end of if

        startNumber += 1
    # end of while

    return primeList[-1]
# end of nthPrime
for i in range(1,20):
    print(nthPrime(i))
