def fib(n):
    # return the nth fib number in the seqeunce

    if n in {0,1}:
        return n
    else:
        return fib(n-1) + fib(n-2)

print('Fib of num is:', fib(6))