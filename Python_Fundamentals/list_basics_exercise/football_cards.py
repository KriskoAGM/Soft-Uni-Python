cards = input().split()
team_a_players_left = 11
team_b_players_left = 11
team_A_sent_off = []
team_B_sent_off = []
insufficient_players = False

for card in cards:
    if card in team_A_sent_off or card in team_B_sent_off:
        continue
    for letter in card:
        if letter == 'A':
            team_A_sent_off.append(card)
            team_a_players_left -= 1
        if letter == 'B':
            team_B_sent_off.append(card)
            team_b_players_left -= 1
    if team_a_players_left < 7 or team_b_players_left < 7:
        insufficient_players = True
        break


print(f"Team A - {team_a_players_left}; Team B - {team_b_players_left}")

if insufficient_players:
    print('Game was terminated')





