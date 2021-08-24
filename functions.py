
# factor finding function
def factors(num):
    '''
    factors() returns a list of all factors of num

    arguments
    -- num: integer

    return
    --list
    '''

    factor_list = [] # empty list to contain factors

    for divider in range(1, num+1):
        # divider will represent all numbers 1 to num

        #check if divided is divisible for num
        if num % divider == 0:
            factor_list.append(divider)
            # .append() method adds a value to the end of a list
            # since factor_list is a list, i can use list methods
        # end of if
    #end of for
    return factor_list
# end of factors()

for numbers in range(10,21):
    print('Factors of', numbers)
    print(factors(numbers))

