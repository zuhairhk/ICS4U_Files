def intInput(prompt = ''):

    userInput = input(prompt)
    invalid = not (userInput.isnumeric() and int(userInput) > 0)

    while invalid:
        print('Invalid entry!')
        userInput = input(prompt)
        invalid = not (userInput.isnumeric() and int(userInput) > 0)
    # end of while

    return int(userInput)


value = intInput('Enter a value:')
