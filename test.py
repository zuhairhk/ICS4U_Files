guess = 6
answer = 4

while guess != answer:
    guess = int(input ("Guess the number: "))

    if guess >= 10:
        print ("The number is less than 10!")

    if guess <= 0:
        print ("The number is greater than 0!")

    if (guess > answer) and (guess < 10):
        print ("Lower!")

    if 0 < guess < answer:
        print ("Higher!")

if guess == answer:
    print ("You got it!")
