import random


print("\nWelcome to Rock, Paper, Scissors!\n")
choice_list = ["R", "P", "S"]
choice_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
run_again = True
while run_again == True:
    player_choice = input("\nPlay[\"R\" for Rock, \"P\" for Paper, \"S\" for Scissors]\n")
    
    # Accept if user enters r, p, or s.
    player_choice = player_choice.upper()
    cpu_choice = random.choice(choice_list)
    if player_choice in choice_list:
        if player_choice == cpu_choice:
            print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
            print(f"\nBoth players selected {choice_dict[player_choice]}. It's a tie!")
            continue
        elif player_choice == "R":
            if cpu_choice == "S":
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nRock smashes Scissors ✂ ! You win!")
            else:
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nPaper covers Rock! CPU wins!")
        elif player_choice == "P":
            if cpu_choice == "R":
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nPaper covers Rock! You win!")
            else:
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nScissors cuts Paper! CPU wins!")

        elif player_choice == "S":
            if cpu_choice == "P":
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nScissors cuts Paper! You win!")
            else:
                print(f"\nPlayer ({choice_dict[player_choice]}) : ({choice_dict[cpu_choice]}) CPU")
                print("\nRock smashes Scissors! CPU wins!")

        break
    else:
        print("\nInvalid input. Please try again.")
        continue
         
       