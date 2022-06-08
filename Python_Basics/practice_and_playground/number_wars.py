player_one_name = input()
player_two_name = input()
player_one_points = 0
player_two_points = 0
winner = ''

while True:
    player_one_card = input()

    if player_one_card == 'End of game':
        print(f"{player_one_name} has {player_one_points} points")
        print(f"{player_two_name} has {player_two_points} points")
        break

    player_two_card = input()

    if int(player_one_card) > int(player_two_card):
        player_one_points += abs(int(player_one_card) - int(player_two_card))

    else:
        player_two_points += abs(int(player_one_card) - int(player_two_card))

    if int(player_one_card) == int(player_two_card):
        print('\nNumber wars!')
        p1_chance_2 = input()
        p2_chance_2 = input()

        if int(p1_chance_2) > int(p2_chance_2):
            winner = player_one_name
            print(f"{winner} is winner with {player_one_points} points")
            break

        else:
            winner = player_two_name
            print(f"{winner} is winner with {player_two_points} points")
            break

