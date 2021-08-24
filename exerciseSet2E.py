def stringInter(word1, word2):
    ''' stringInter() returns common characters between the arguement
    arg
    -- word1 : string
    -- word2 : string

    return
    -- string
    '''

    result = ''

    for char in word1:
        if char in word2 in word2 and char not in result:
            result += char

    return result
# end


print(stringInter('Hello', 'Goodbye'))
