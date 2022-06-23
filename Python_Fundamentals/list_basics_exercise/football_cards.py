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
            break
        elif letter == 'B':
            team_B_sent_off.append(card)
            team_b_players_left -= 1
            break
    if team_a_players_left < 7 or team_b_players_left < 7:
        insufficient_players = True
        break

print(f"Team A - {team_a_players_left}; Team B - {team_b_players_left}")

if insufficient_players:
    print('Game was terminated')


# Second solution
# team_a = ["A-" + str(x) for x in range(1, 11 + 1)]
# team_b = ["B-" + str(x) for x in range(1, 11 + 1)]
#
# sent_off_players = input().split()
# insufficient_players = False
#
# for player in sent_off_players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         insufficient_players = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if insufficient_players:
#     print("Game was terminated")
