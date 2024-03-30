import random


def getOptions():
  options = ('rock', 'paper', 'scissors')
  userOption = input('Rock, paper or scissors => ')
  userOption = userOption.lower()

  if not userOption in options:
    print('Invalid option')
    return None, None

  computerOption = random.choice(options)

  print('User option =>', userOption)
  print('Bot option =>', computerOption)
  return userOption, computerOption


def checkRules(userOption, computerOption, userWins, computerWins):
  if userOption == computerOption:
    print('Tie!')
  elif userOption == 'rock':
    if computerOption == 'scissors':
      print('Rock wins!')
      print('User wins!')
      userWins += 1
    else:
      print('Paper wins!')
      print('Bot wins!')
      computerWins += 1
  elif userOption == 'paper':
    if computerOption == 'rock':
      print('Paper wins!')
      print('User wins!')
      userWins += 1
    else:
      print('Scissors wins!')
      print('Bot wins!')
      computerWins += 1
  elif userOption == 'scissors':
    if computerOption == 'paper':
      print('Scissors wins!')
      print('User wins!')
      userWins += 1
    else:
      print('Rock wins!')
      print('Bot wins!')
      computerWins += 1

  return userWins, computerWins

def runGame():
  computerWins = 0
  userWins = 0
  rounds = 1

  while True:
    print('*' * 10)

    print('ROUND', rounds)
    print('*' * 10)
    print('Computer wins', computerWins)
    print('User wins', userWins)
    rounds += 1

    userOption, computerOption = getOptions()
    if (userOption == None or computerOption == None): 
      continue
    
    userWins, computerWins = checkRules(userOption,
                                        computerOption, userWins,
                                        computerWins)
    if computerWins == 2:
      print('Bot is the winner!')    
      break

    if userWins == 2:
      print('User is the winner!')    
      break
      
runGame()
