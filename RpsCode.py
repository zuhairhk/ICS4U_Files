# RockPaperScissors
# Made by: Zuhair H. Khan
# Date: 2021-03-04

import random

def nameGenerator(num):
    '''
    nameGenerator() generates a list of randomized names
    arg:
    -- num : integer

    return
    -- fullName : list
    '''

    #list with first names
    firstName = ['Naruto', 'LeLouch', 'Lionel', 'Monkey D.', 'Cristiano', 'Son', 'Lightning', 'Shoto', 'Eren', 'John']
    #list with last names
    lastName = ['Uzumaki', 'Lampouch', 'Messi', 'Luffy', 'Ronaldo', 'Goku', 'McQueen', 'Nagisa', 'Jaeger', 'Arnold']

    fullName = [' '] * num

    #list of first names randomized
    nFirst = random.sample(firstName, num)
    #list of last names randomized
    nLast = random.sample(lastName, num)

    #assigns the randomized first names and last names to an index in the list giving each player a full name
    for i in range(num):
        fullName[i] = (nFirst[i] + ' ' + nLast[i])
    
    print()
    print('Players are:', fullName)
    
    return fullName


def matchUp(names, repeat, loserList, wList, count):
    '''
    matchUp() pairs players against each other until there is a winner
    arg:
    -- names : list
    -- repeat : integer
    -- loserList : list
    -- wList : list
    -- count : integer
    '''

    x = 0
    player = [' '] * (len(names))
    winnerList = []
    losers = []

    #randomizes the order of the player list in order to randomly pair players
    randMatch = random.sample(names, len(names))

    for i in range(len(names)):
        player[i] = randMatch[i]

    #loop repeats enough times to match up each player
    while x in range(int((len(names)) / 2)):
        print()
        print('Round', repeat, 'Match', x + 1, 'results:')

        #player1 starts at the beginning of the list and iterates forward by 1 index at a time
        player1 = player[x]
        #player2 starts at the end of the list and iterates backwards by 1 index at a time 
        player2 = player[len(names) - x - 1]
        #player3 is the player in the middle of the list (used for instances where there are an odd number of players)
        player3 = player[(int((len(names)) / 2))]

        #calls the rock rockPaperScissors method to make players compete
        playerResults = rockPaperScissors(player1, player2, names)

        #the rockPaperScissors function returns a tuple containing the winner, loser, and a sentence stating how the winner won the tournament(used in the last round)
        winner = playerResults[0]
        loser = playerResults[1]
        fStatement = playerResults[2]

        #list of current winner(s)
        winnerList.append(winner)
        #list of every winner
        wList.append(winner)

        #if number of players is odd, the player in the middle of the list is told to sit out this round and get ready to fight the next round
        if len(names) % 2 != 0 and (player3 not in winnerList):
            winnerList.append(player3)
        
        #creates a list to keep track of all of the losers
        if winner in winnerList:
            if player1 == winner or player2 == winner:
                loserList.append(loser)
       
        print(winner, 'beat', loser)
        print(loser, 'had a bye... :(')
        print()

        x += 1

    #if there are more than 1 winners, repeat the function
    if len(winnerList) > 1:
        repeat += 1
        matchUp(winnerList, repeat, loserList, wList, count)
    else:
        tWinner = winnerList[0]
        
        #checks every index of when the tournament winner won a battle and then appends the loser of that index to a list of the winners opponents
        for i in range(len(wList)):
            if tWinner == wList[i]:
                losers.append(loserList[i])

        print('Winner is:', tWinner)
        print(fStatement, 'in the final battle!')
        print(tWinner, 'defeated', losers)


def rockPaperScissors(player1, player2, names):
    '''
    rockPaperScissors() executes the rock paper scissors game with given players
    arg:
    -- player1 : string
    -- player2 : string
    -- names : list

    return:
    -- tuple containing winner and loser of the current battle and, a sentence stating how the tournament winner won in the final battle
    '''
    
    statement = ''

    #assigns each player a choice where we let rock be 0, paper be 1, and scissors be 2
    p1Choice = random.randrange(0,3)
    p2Choice = random.randrange(0,3)

    #p1Choice cannot be the same as p2Choice
    while p1Choice == p2Choice:
        p1Choice = random.randrange(0,3)
        p2Choice = random.randrange(0,3)
    
    #if it is not the last round
    if len(names) > 2:
        if p1Choice == 0:
            if p2Choice == 1:
                #p1:rock vs p2:paper
                winner = player2
                loser = player1
            elif p2Choice == 2:
                #p1:rock vs p2:scissors
                winner = player1
                loser = player2
        
        if p1Choice == 1:
            if p2Choice == 0:
                #p1:paper vs p2:rock
                winner = player1
                loser = player2
            elif p2Choice == 2:
                #p1:paper vs p2:scissors
                winner = player2
                loser = player1
        
        if p1Choice == 2:
            if p2Choice == 0:
                #p1:scissors vs p2:rock
                winner = player2
                loser = player1
            elif p2Choice == 1:
                #p1:scissors vs p2:paper
                winner = player1
                loser = player2
    
    #During last battle, additional str variable is used to state how the winner won
    elif len(names) == 2:
        if p1Choice == 0:
            if p2Choice == 1:
                winner = player2
                loser = player1
                statement = ('Won with paper over rock')
            elif p2Choice == 2:
                winner = player1
                loser = player2
                statement = ('Won with rock over scissors')
        
        if p1Choice == 1:
            if p2Choice == 0:
                winner = player1
                loser = player2
                statement = ('Won with paper over rock')
            elif p2Choice == 2:
                winner = player2
                loser = player1
                statement = ('Won with scissors over paper')
        
        if p1Choice == 2:
            if p2Choice == 0:
                winner = player2
                loser = player1
                statement = ('Won with rock over scissors')
            elif p2Choice == 1:
                winner = player1
                loser = player2
                statement = ('Won with scissors over paper')
    
    return (winner, loser, statement)


#Main
loserList = []
wList = []

print('--------------------------------------------------------------')
print('Get ready for the TEJ4M Rock Paper Scissors Championship!!!')
print('--------------------------------------------------------------')

players = int(input('Enter # of players:'))

#number of players has to be at least 2 and less than 10
while players > 10 or players < 2:
    print('Inavlid entry. Please try again!')
    players = int(input('Enter # of players:'))

ans = input('Are you ready to start -----> (y to begin)')

#answer has to be lower case 'y'
while ans != 'y':
    print('Inavlid entry. Please try again!')
    ans = input('Are you ready to start -----> (y to begin)')

#function executed when given valid inputs
if ans == 'y':
    matchUp((nameGenerator(players)), 1, loserList, wList, 0)