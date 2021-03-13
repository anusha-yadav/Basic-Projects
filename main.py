#Rock Paper Scissor Game
import random
CompChoice=["Rock","Scissor","Paper"]
while 1:
    print("Rock Paper Scissor Game")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("Round ",i,"Start")
        print("Select any one option")
        print("1. Rock","2. Paper","3. Scissor",sep='\n')
        x=int(input())
        if x==1:
            print("You select rock")
            x="Rock"
        elif x==2:
            print("You select paper")
            x="Paper"
        elif x==3:
            print("You select scissor")
            x="Scissor"
        else:
            print("Invalid Choice")
            break
        ComputerChoice=random.choice(CompChoice)
        print("The computer selects: ",ComputerChoice)
        if (x==ComputerChoice):
            youwin+=1
            computerwin+=1
            print("This round is draw")
        elif (x=="Paper" and ComputerChoice=="Rock") or (x=="Rock" and ComputerChoice=="Scissor") or(x=="Scissor" and ComputerChoice=="Paper"):
            youwin+=1
            print("You win this round")
        else:
            computerwin+=1
            print("Computer wins this round")
    if youwin>computerwin:
        print("You win this game")
        print("Your score is: ",youwin,"Computer Score is: ",computerwin,sep=" ")
    elif computerwin>youwin:
        print("Computer win this game")
        print("Your score is: ", youwin, "Computer Score is: ", computerwin, sep=" ")
    else:
        print("Match Draw")
        print("Your score is: ", youwin, "Computer Score is: ", computerwin, sep=" ")
    user_choice=input("Want to play again?(Yes/Exit)")
    if user_choice=='yes' or user_choice=="Yes":
        continue
    else:
        break
