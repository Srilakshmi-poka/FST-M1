
def play():
    player1= str(input("Enetr the player1 option:"))
    player2=str(input("Enetr the player2 option:"))
    if player1==player2:
        print("it is a tie")
    elif player1=="Rock":
        if player2=="Scissors":
            print("Player1 wins")
        elif player2=="Paper":
            print("Player2 wins")
    elif player1=="Scissors":
        if player2=="Paper":
            print("player1 wins")
        elif player2=="Rock":
            print("Player2 wins")
    elif player1=="Paper":
        if player2=="Rock":
           print("player1 wins")
        elif player2=="Scissors":
            print("Player2 wins")
    
    cont_play = str(input("do you want to play again? Y/N:"))
    if cont_play in ['Y','y']:
        play()    
    else:
        print("Thank you! Bye Bye!!!")
    
play()



    