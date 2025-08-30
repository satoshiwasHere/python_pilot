import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        # data type creates a collection of name value pairs
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerChoice = input(
            "\nEnter ...\n1 for Rock,\n2 for paper,\n3 or scissors\n\n"
        )

        if playerChoice not in ["1", "2", "3"]:
            print("please choose 1, 2 or 3.")
            return play_rps()

        playa = int(playerChoice)

        # random.choice() function picks a single element randomly from a sequence.
        # sequence = string "123", which is treated as a list of characters
        # computerChoice will be assigned either the character

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print("\nyou chose " + str(RPS(playa)).replace("RPS.", " ") + ".")
        print("Pyhon3 chose " + str(RPS(computer)).replace("RPS.", " ") + ".\n")

        def decide_winner(playa, computer):
            nonlocal player_wins
            nonlocal python_wins
            if playa == 1 and computer == 3:
                player_wins += 1
                return "You win 🎊 🎉"
            elif playa == 2 and computer == 1:
                player_wins += 1
                return "🎊 🎉you win"
            elif playa == 3 and computer == 2:
                player_wins += 1
                return "🎊 🎉you win"
            elif playa == computer:

                return "🙃 Its a tie, Try Again!"

            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(playa, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count " + str(game_count))
        print("\nplayer wins " + str(player_wins))
        print("\npython wins " + str(python_wins))

        print("\nplay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to quit\n")
            if playagain.lower() not in ["y", "Q"]:
                continue
            else:
                break

        if playagain == "y":
            return play_rps()
        else:
            print("\n🎊🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye 👋")

    return play_rps()


play = rps()

play()
