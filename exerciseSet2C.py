def dupFinder(word):
    '''
    dupFinder() returns a string with characters that occur more than once
    arg:
    -- sequence: string or list
    return:
    -- string
    '''

    result = ''

    for char in word:
        if word.count(char) >= 2 and char not in result:
            result += char

    return result


print(dupFinder('Hello World!'))
