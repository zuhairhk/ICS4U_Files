'''
print(list(range(10)))

# range(n) will generate all integers from [0,n)
for i in range(10):
    print(i)

for j in range(10, 20):
    print(j)

# a has to be < than b

for k in range (10,100,10):
    print(k)
#prints all integers from a to b with c as an interval
'''

'''
# input
n = int(input(('Enter a number greater than -1')))

# while loop solution
fib0 = 0
fib1 = 1
fibN = 0

# base cases
if n == 0:
    print(fib0)
elif n == 1:
    print(fib1)
else:
    location = 2

    while location <= n:
        fibN = fib1 + fib0
        fib0 = fib1
        fib1 = fibN

        location += 1
    # end of while
    print(fibN)
'''
# input
n = int(input(('Enter a number greater than -1')))

# for loop solution
fib0 = 0
fib1 = 1
fibN = 0

if n == 0:
    print(fib0)
elif n == 1:
    print(fib1)
else:
    location = 2
    for i in range(2, n+1):
        fibN = fibN = fib1 + fib0
        fib0 = fib1
        fib1 = fibN

    # end of for
    print(fibN)
