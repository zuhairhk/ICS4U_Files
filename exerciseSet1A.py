def even(num):
    '''
    even() checks if number is even

    arguments
    -- num: integer

    return
    --boolean (True for Yes, False for No)
    '''

    if num % 2 == 0:
        ans = True
    else:
        ans = False

    return ans

num = int(input('Enter a number'))
print(even(num))
'''
ICS3U - U6E1 - Exercise Set 1

Exercise A: Create an even number checking function
Parameter: Integer
Returns: Boolean (True for Yes, False for No)

Exercise B: Create a Palindrome checking Function
Parameter: a String
Returns: Boolean (True for Yes, False for No)

Exercise C: Create a Prime Number checking Function
Parameter: a number
Returns: Boolean (True for Yes, False for No)

Exercise D: Create a Vowel Counting Function
Parameter: String
Returns: Integer

Exercise E: Create a Factorial Calculator
Parameter: integer
Output: integer

Exercise F: Create a Nth Prime Number finding function
Parameter: N: integer
Output: the prime number
'''