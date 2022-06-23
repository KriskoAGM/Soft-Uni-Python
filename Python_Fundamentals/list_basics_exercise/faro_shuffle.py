# cards = input().split()
# shuffles = int(input())
#
# for card in range(shuffles):
#     shuffled_deck = []
#     middle_of_deck = len(cards) // 2
#     left_part = cards[0:middle_of_deck]
#     right_part = cards[middle_of_deck::]
#
#     for index in range(len(left_part)):
#         shuffled_deck.append(left_part[index])
#         shuffled_deck.append(right_part[index])
#
#     cards = shuffled_deck
# print(cards)

deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    final_deck = []
    middle = len(deck) // 2
    left_part = deck[0:middle]
    right_part = deck[middle::]

    for i in range(len(left_part)):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])

    deck = final_deck
print(deck)

























