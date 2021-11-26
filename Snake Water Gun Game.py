import random

Cchoice = ["Snake", "Water", "Gun"]

while True:
    # Begining the game
    print("** WELCOME TO SNAKE  WATER  GUN  GAME: ***")

    Name = input("Plese Enter Your Name : ")

    youwin, computerwin = 0, 0

    # Making The Game of 5 Rounds
    for i in range(1, 4):
        print("Round", i, "Start:")
        print("Please select any one option: ")
        print("1.Snake ", "2.Water ", "3.Gun ", sep="\n")

        # Teling what you have choosen
        Yourchoice = int(input())
        print()
        if Yourchoice == 1:
            print(f"{Name} selected: Snake ")
            Yourchoice = "Snake"
        elif Yourchoice == 2:
            print(f"{Name} selected: Water ")
            Yourchoice = "Water"
        elif Yourchoice == 3:
            print(f"{Name} selected: Gun ")
            Yourchoice = "Gun"
        else:
            print("Invalid Choice")
            break
        # random select by computer
        Computerchoice = random.choice(Cchoice)
        print("Computer selected:", Computerchoice)

        # If Both Are Selected Same Choice Round Is Drawn
        if Yourchoice == Computerchoice:
            youwin += 1
            computerwin += 1
            print("This Round is Draw:")
            print()

        elif (Yourchoice == "Gun" and Computerchoice == "Snake") or (Yourchoice == "Snake" and Computerchoice == "Water") or (Yourchoice == "Water" and Computerchoice == "Gun"):
            youwin += 1
            print(f"{Name} win this Round  !!! \n ")
            print()
        else:
            computerwin += 1
            print("Computer win this Round  !!! \n ")
            print()

# Declaring Scores Based On Whose Score is greater
    if youwin > computerwin:
        print(f"*** {Name} Win the game !!! ***" "\n"  "Computer Lose the game. ")
        print(f"Score is:\n{Name} score:", youwin, "\n"
              "Computer score:", computerwin, sep=" ")
    elif computerwin > youwin:
        print(f"{Name} Lose the game." "\n"  "*** Computer win the game !!! ***")
        print(f"Score is:\n{Name} score:", youwin, "\n"
              "Computer score:", computerwin, sep=" ")
    else:
        print("** The Match Is Draw **")
        print(f"Score is:\n{Name} score:", youwin, "\n"
              "Computer score:", computerwin, sep=" ")
    user_choice = input("Want to Play again?(Yes/Exit)\n")
    if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
        continue
    else:
        break
