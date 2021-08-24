def avgFinder(nums):
    '''
    avg() finds the average of a given float/integer-based list
    arg:
    -- nums : list
    return:
    -- avg : int
    '''

    i = 0
    num1 = 0

    while i < 4:
        num1 = nums[i] + num1
        i += 1
    # end of for

    avg = num1/4

    return avg


print('Average is', avgFinder([99, 97, 94, 98]))
