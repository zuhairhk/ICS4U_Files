'''
def factors(num):

    result = []

    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)

    return result


print(12, factors(12))


def factors2(num):

    result = []

    limit = int((num ** 0.5)) + 1
    interval = 1

    if num % 2 != 0:
        interval += 1

    # print('limit:', limit)
    # print('interval:', interval)

    for divider in range(1, limit, interval):
        # print('Current divider:', divider)
        if num % divider == 0:
            other = num // divider
            if other == divider:
                result.append(divider)
            else:
                result.append(divider)
                result.append(other)
    return result


print(factors2(12))
'''

'''
def primeFactors(num):

    result = []

    while num % 2 == 0:
        result.append(2)
        num //= 2

        if num == 1:
            return result

    divider = 3

    while num != 1:
        if num % divider == 0:
            result.append(divider)
            num //= divider
        else:
            divider += 2

    return result


print(64, primeFactors(64))
print(7200, primeFactors(7200))
'''

def prime(num):

    list = []

    i = 1

    while i <= num:
        list.append(i)
        i += 1

    print(list)

    result = []

    limit = int((num ** 0.5)) + 1

    



print(prime(12))
