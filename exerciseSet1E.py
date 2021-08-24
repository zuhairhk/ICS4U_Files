def fCalc(num):
    '''
    argument
    -- num: integer
    return
    --
    num: integer
    '''

    count = 0
    
    n = 1

    num2 = num

    while count < num-1:
        num1 = num2 * (num-n)

        num2 = num1
        count += 1
        n += 1
    # end of while

    return num1


num = int(input('Enter an int number'))
print(fCalc(num))
