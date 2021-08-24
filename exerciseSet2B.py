def consCount(word):
    '''
    consCount() counts the number of consonants in a word
    arg:
    -- word: string
    reutrn:
    -- num: int
    '''

    count = 0

    for char in word:
        if char.isalpha() and char.lower() not in 'aeiou':
            count += 1
        # end of if
    # end of for

    return count


print(consCount('Ooga Booga'))
