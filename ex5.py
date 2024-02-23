import random

def ComputerSelection():
    randomNumber = random.randint(0, 2)
    if (randomNumber == 0):
        return 'g'
    elif (randomNumber == 1):
        return 'w'
    else:
        return 's'

def CheckAnswer(userChoice, computerChoice):
    if (userChoice == "w" and computerChoice == "g"):
        return 1
    elif (userChoice == "g" and computerChoice == "s"):
        return 1
    elif (userChoice == "s" and computerChoice == "w"):
        return 1
    elif(userChoice == "g" and computerChoice == "w"):
        return -1
    elif (userChoice == "s" and computerChoice == "g"):
        return -1
    elif (userChoice == "w" and computerChoice == "s"):
        return -1 
    elif (userChoice == "w" and computerChoice == "w"):
        return 0
    elif (userChoice == "s" and computerChoice == "s"):
        return 0
    elif (userChoice == "g" and computerChoice == "g"):
        return 0
    else:
        return None

def CheckWinner(userScore, computerScore):
    if (userScore > computerScore):
        return f"User Won this Match | User: {userScore} - Computer: {computerScore}"
    elif (computerScore > userScore):
        return f"Computer Won this Match | User: {userScore} - Computer: {computerScore}"
    else:
        return f"Match is Tie | User: {userScore} - Computer: {computerScore}"

i = 0
computerScore = 0
userScore = 0
while (i < 10):
    userInput = input("Enter you answer (g, w, s): ")
    computerSelect = ComputerSelection()
    print("Computer Selected: " + computerSelect)
    answer = CheckAnswer(userInput, computerSelect)
    if (answer == 1):
        print("User Won")
        userScore += 1
    elif (answer == -1):
        print("Computer Won")
        computerScore += 1
    else:
        print("Tie")
    i +=1


print(CheckWinner(userScore, computerScore))