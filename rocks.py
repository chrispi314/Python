import random

def randomChoice():
    choices = ["Rock", "Paper", "Scissors"]
    return(random.choice(choices))

def winner(player1, player2):
    if player1 == player2:
        return("Tie!")
    if player1 == "Rock" and player2 == "Paper":
        return("player2 is Winner!")
    if player1 == "Rock" and player2 == "Scissors":
        return("player1 is Winner!")
    if player1 == "Paper" and player2 == "Rock":
        return("player1 is Winner!")
    if player1 == "Paper" and player2 == "Scissors":
        return("player2 is Winner!")
    if player1 == "Scissors" and player2 == "Rock":
        return("player2 is Winner!")
    if player1 == "Scissors" and player2 == "Paper":
        return("player1 is Winner!")
    
def game():
    player1 = randomChoice()
    player2 = randomChoice()

    print("player1 picked: " + player1)
    print("player2 picked: " + player2)
    print(winner(player1, player2))
game()
