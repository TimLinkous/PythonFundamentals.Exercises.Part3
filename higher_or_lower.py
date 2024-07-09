from random import randrange

def give_me_a_num():
    #print("Give a number between 1 and 10\n")
    player_num = input("Give a number between 1 and 10\n")
    return int(player_num)

def random_num():
    return randrange(1,10)
    
def evaluate_numbers():
    one = give_me_a_num()
    two = random_num()

    if one > two:
        print("Your guess is too high\nThe correct number was ", two, "\nYour guess was ", one)
    elif one < two:
        print("Your guess is too low\nThe correct number was ", two, "\nYour guess was ", one)
    else:
        print("Congratulations!! You guessed the correct number!")

evaluate_numbers()