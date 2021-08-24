def endGame():
    print('Thank you for playing!')
    return


#Function that does not take in or return a value
def rockpaperscissors():
  win = 0
  repeat = 'y'
  answer = 1
#While loop with condition to exit
  while repeat == 'y' and (answer == 1 or answer == 2): 
      games = int(input("How many games do you want? "))

      #Use a for loop to repeat a certain number of times
      for i in range(games):
          playerChoice = input("rock, paper, scissors? ")

          #Check to make sure the user enters rock, paper or scissors and repeat until it is right
          while playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
              print('Invalid Entry, Try Again!')
              playerChoice = input("rock, paper, scissors?")

          #Generate a random choice of rock, paper, scissors for the computer
          computerChoice = random.randrange(3)
          if computerChoice == 0:
              computer = "rock"
              print('Computer picked', computer)
          elif computerChoice == 1:
              computer = "paper"
              print('Computer picked', computer)
          elif computerChoice == 2:
              computer = "scissors"
              print('Computer picked', computer)

          #Compare computer values to player values to determine a winner or tie
          if playerChoice == computer: 
              print ("Draw")
          elif playerChoice == "rock":
              if computer == "scissors":
                  print ("You Win!")
                  win += 1
              if computer == "paper":
                  print ("You Lose!")
          elif playerChoice == "paper":
              if computer == "rock":
                  print ("You Win!")
                  win += 1
              if computer == "scissors":
                  print ("You Lose!")
          elif playerChoice == "scissors":
              if computer == "paper":
                  print ("You Win!")
                  win += 1
              if computer == "rock":
                  print ("You Lose!")
  
      #Track winner games and wins and output it at the end
      print('You played', games, 'times and won', win, 'times')
  
      answer = input("Which Game Do You Want To Play? 1 or 2 or anything else to exit? ")

      if answer == "1":
          rockpaperscissors()
      elif answer != "1":
          if answer == "2":
              gymBattle()  
          else:
              endGame()
      


def pickNum():
  n = random.randint(0,5)
  
  return n


def gymBattle():
#Instructions on how to play with a print statement
  print()
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("You will be given the choice to pick between 1 of the 3 pokemon types fire, water, and grass.")
  print("based on your desicion you will be assigned a random pokemon with a random move of its type.")
  print("Your pokemon will go up against a random cpu pokemon and you will win, draw, or lose based on the condition")
  print("The condition is that fire beats grass, grass beats water, and water beats fire.")
  print("Good Luck and Have Fun!")
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print()

  firePokemon = ["Charizard" , "Blazikin",  "Infernape"]
  
  waterPokemon = ["Blastiose", "Swampert","Empoleon"]
  
  grassPokemon = [ "Venasuar","Sceptile", "Torterra"]
  #Use a tuple
  waterMoves = ('Aqua Wave', 'Water Blast', 'Hydro Beam', 'Bubble Rasengan', 'Whirl Cannnon','Neslay pool')
  
  fireMoves = ('Majestic Flame', 'Heat blast', 'Fire Ball', 'Dragon Flame Cannon', 'Hot rise', 'Amaterasu')
  
  grassMoves = ('Life absorb', 'Energy Beam', 'Wood Dragon', 'Grass cannon', 'Vine Trap', 'Solar meteorite')

  print('----------------------------------------------------')
  choice = int(input('Enter pokemon type: 0 for fire, 1 for water, 2 for grass '))
  print('----------------------------------------------------')
  

  #There will be 3 battles ... so 3 winners
  count = 0
  winnersList = []
  while count < 3:
      if count == 0:
          print()
          print('**** ROUND 1 ****')
          print()
      if count == 1:
          print()
          print('**** ROUND 2 ****')
          print()
      if count == 2:
          print()
          print('**** ROUND 3 ****')
          print()
      randNum = random.randrange(0,3)
      #If, elif, else statement
      if choice == 0:
          playerPokemon = firePokemon[randNum]
          playerMove = fireMoves[pickNum()]
      elif choice == 1:
          playerPokemon = waterPokemon[randNum]
          playerMove = waterMoves[pickNum()]
      elif choice == 2:
          playerPokemon = grassPokemon[randNum]
          playerMove = grassMoves[pickNum()]  


      player = (playerPokemon + ' who has the move ' + playerMove)

      print("You have", player)

      #Use of random function
      computerChoice = random.randrange(3)
      if computerChoice == 0:
          computer = firePokemon[randNum]
          computerMove = fireMoves[pickNum()]
          print('Computer has', computer, 'and has the move', computerMove)
      elif computerChoice == 1:
          computer = waterPokemon[randNum]
          computerMove = waterMoves[pickNum()]
          print('Computer has', computer, 'and has the move', computerMove)
      elif computerChoice == 2:
          computer = grassPokemon[randNum]
          computerMove = grassMoves[pickNum()]
          print('Computer has', computer, 'and has the move', computerMove)

      
      winner = gymFight(choice, computerChoice, playerPokemon, playerMove, computer, computerMove)

      print()
      print("Winner is" , winner)
      print()

      if winner != 'no winner':
          #Append or remove an item from a list
          winnersList.append(winner)
      
      count += 1
  
  numOfWinners = 0
  #For loop
  for i in range(len(winnersList)):
      numOfWinners += 1

  print('---------------------------------------------------------------------------')
  print('The', numOfWinners, 'winner(s) for the gym battles were:', winnersList)
  print('---------------------------------------------------------------------------')
  
  answer = input("Which Game Do You Want To Play? 1 or 2 or anything else to exit? ")

  if answer == "1":
      print('entered the loop')
      rockpaperscissors()
  elif answer == "2":
        gymBattle()  
  else:
      endGame()


#0=fire, 1=water, 2=grass
#Function that takes in a data type and returns one
def gymFight(choice, computerChoice, playerPokemon, playerMove, computer, computerMove):
  #Use of a string
  winner = " "
  if choice == computerChoice: 
      winner = 'no winner'
  
  elif choice == 0:
      if computerChoice == 2:
          print ("You Win!")
          winner = playerPokemon
      if computerChoice == 1:
          print ("You Lose!")
          winner = computer      
  
  elif choice == 1:
      if computerChoice == 0:
          print ("You Win!")
          winner = playerPokemon
      if computerChoice == 2:
          print ("You Lose!")
          winner = computer
  
  elif choice == 2:
      if computerChoice == 1:
          print ("You Win!")
          winner = playerPokemon
      if computerChoice == 0:
          print ("You Lose!")  
          winner = computer
  
  return winner



import random
answer = input("Which Game Do You Want To Play? 1 or 2 or anything else to exit? ")

if answer == "1":
  rockpaperscissors()
elif answer != "1":
  if answer == "2":
      gymBattle()  
  else:
      endGame()