def prime(num):
    '''
    prime() checks if number is prime or not

    arguments
    -- num: integer

    return
    --boolean (True for Yes, False for No)
    '''

    if num < 2:
        return False
    elif num in [2, 3]:
        return True
    elif num % 2 == 0:
        return False
    else:
        for divider in range(3, int(num ** 0.5) + 1):
            if num % divider == 0:
                return False
        # end of for
        return True  # it should prime number here
    # end of isPrime


num = int(input('Enter a number'))

print(prime(num))
