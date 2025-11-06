import getpass




def playRPS():
    rpc1 = getpass.getpass('player one what do you want to be rock, paper, or scissors')
    rpc2 = getpass.getpass('player two what do you want to be rock, paper, or scissors')
    if rpc1 == 'rock' and rpc2 == 'paper':
         print("player two wins")
         print("player one is a loser")
         print("player two eat player one")

    elif rpc1 == 'paper' and rpc2 == 'scissors':
         print("player two wins")
         print("player one is a loser")
         print("player one give player two a soda")

    elif rpc1 == 'scissors' and rpc2 == 'rock':
         print("player two wins")
         print("player one is a loser")
         print("player two gets one free hit")

    elif rpc1 == 'paper' and rpc2 == 'rock':
         print("player one wins")
         print("player two is a loser")
         print("player two give player one a white monster")
    
    elif rpc1 == 'scissors' and rpc2 == 'paper':
         print("player one wins")
         print("player two is a loser")
         print("player one beet player two with a stick")

    elif rpc1 == 'rock' and rpc2 == 'sicssor':
         print("player one wins")
         print("player two is a loser")
         print("player one tell player two he/she has a baby face!")

    else:
         print("error") 
         print("tie or invalid anser")      




answer = input('wnat to play  rock paper scissors?')
while answer == 'yes':
    print ("get ready to play mostest bestest bigest gameest of rock paper scissorest")
    playRPS()
    answer = input('wnat to play  rock paper scissors?')

    
print(" your a loser now go away")

