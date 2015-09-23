import random 
   
enemyInput = random.randint(1,5)
playerInput = int(input("Rock? input 1  ||  Paper? input 2  ||  Scissors? input 3 || Lizard? input 4 || Spock? input 5"))

if enemyInput == 1 :
    if playerInput == 1:
        print("Tie! Rock cancels Rock")
    if playerInput == 2:
        print("You Win! Paper beats Rock")
    if playerInput == 3:
        print("You Lose! Rock beats Scissors") 
    if playerInput == 4: 
        print("You Lose! Rock beats Lizard")
    if playerInput == 5:
        print("You win! Spock beats Rock")

if enemyInput == 2 :
    if playerInput == 1:
        print("You lose! Paper beats Rock")
    if playerInput == 2: 
        print("Tie! Paper cancels Paper")
    if playerInput == 3: 
        print("You Win! Scissors beat Paper")
    if playerInput == 4: 
        print("You win! Lizard beats Paper")
    if playerInput == 5: 
        print("You Lose! Paper beats Spock")

if enemyInput == 3: 
    if playerInput == 1:
        print("You Win! Rock beats Scissors")
    if playerInput == 2: 
        print("You Lose! Scissors beat Paper")
    if playerInput == 3: 
        print("Tie! Scissors cancel Scissors")
    if playerInput == 4:
        print("You lose! Scissors beat Lizard")
    if playerInput == 5:
        print("You win! Spock beats Scissors")

if enemyInput == 4:
    if playerInput == 1:
        print("You win! Rock beats Lizard")
    if playerInput == 2: 
        print("You lose! Lizard beats Paper")
    if playerInput == 3:
        print("You win! Scissors beats Lizard")
    if playerInput == 4: 
        print("Tie! Lizards are too busy fucking to give a shit")
    if playerInput == 5: 
        print("You Lose! Lizard beats Spock")

if enemyInput == 5:
    if playerInput == 1:
        print("You Lose! Spock beats Rock")
    if playerInput == 2: 
        print("You win! Paper beats Spock")
    if playerInput == 3: 
        print("You Lose! Spock beats Scissors")
    if playerInput == 4: 
        print("You win! Lizard beats Scissors")
    if playerInput == 5:
        print("Tie! Spock cancels Spock")

