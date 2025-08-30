# closure is afunction having access to the scope of its parent function,
# after the parent function has returned
# elif checks multiple conditions one after another (if True)
# closure helps in accesing vars without making them global


def parent_function(person, coin):
    # coin = 3

    def play_game():
        nonlocal coin
        coin -= 1

        if coin > 1:
            print("\n" + person + " has " + str(coin) + " coins left")
        elif coin == 1:
            print("\n" + person + " has " + str(coin) + " coin left")
        else:
            print("\n" + person + " is out of coins. ")

    return play_game


tommy = parent_function("Tommy", 5)
jenny = parent_function("jenny", 8)

tommy()
tommy()
jenny()
