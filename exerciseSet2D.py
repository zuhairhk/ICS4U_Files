def search(word, val):
    '''
    search() searches for val in word assuming val is a single character
    arg:
    -- sequence: string
    -- val: string

    return:
    -- integer, -1 if not found
    '''

    count = 0

    for location, value in enumerate(word):
        #print(location, value)
        if value == val:
            return location
        # end of if
    # INSHALLAH I WILL GET ACCEPTED INTO EVERY SINGLE UNIVERSITY THAT I HAVE APPLIED TO
    # end of for
    return -1

print(search('hello world', 'w'))
