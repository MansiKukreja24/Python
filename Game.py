def display_game(game_list):
    print("Here is the current list")
    print(game_list)


def position_choice():
    choice='wrong'
    while choice not in game_list:
        choice=input("Pick a position from gamelist: ")

        if choice not in game_list:
            print("Sorry Wrong Choice")

    return int(choice)


def rep_choice(game_list, position):
    user_rep = input("Type a string to place at the position:  ")
    game_list[position]=user_rep
    return game_list

def game_on_choice():
    choice = 'wrong'
    while choice not in ['y','n']:
        choice = input("Keep playing? ['y','n']: ")

        if choice not in ['y','n']:
            print("Sorry cannot understand choose either 'y' or 'n ")

    if choice=='y':
        return True
    else:
        return False






game_on = True
game_list = list(input("Enter game_list:  "))

while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=rep_choice(game_list,position)
    display_game(game_list)

    game_on=game_on_choice()










