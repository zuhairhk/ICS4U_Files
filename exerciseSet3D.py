def fib(location):
    '''fib() returns the fibonacci number locting at the given location
    '''

    fibSequence = [0,1]
    while len(fibSequence) <= location:
        fibSequence.append(fibSequence[-1] + fibSequence[-2])

    return fibSequence[location]


print(fib(10))
