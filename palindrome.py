def isPalindrome(word):
    '''
    isPalindrome() returns true if the word is a palindrome
    arg
    -- Word : string
    return
    -- Boolean
    '''

    clean_word = word.lower()# .lower() makes all the characters lowercased

    # assuming word has no special characters or numbers

    clean_word = list(word)
    reversed_word = list(reversed(clean_word))

    # compare clean_word vs reversed_word
    for i in range(0, len(clean_word)):
        if clean_word[i] != reversed_word[i]:
            # not a palindrome
            return False
        # end of if
    # end of for
    return True
# end of palindrome


print(isPalindrome('Hello'))

print(isPalindrome('racecar'))
