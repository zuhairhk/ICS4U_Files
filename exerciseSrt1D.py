def vowCount(word):
    ''' vowelCounter counts the number of vowels.
    argument
    -- word : string
    return
    -- integer
    '''

    counter = 0

    for character in word:
        if character.lower() in 'aeiou':
            counter += 1
        #end of if
    #end of for

    return counter


word = input('Enter word: ')
print(vowCount(word))