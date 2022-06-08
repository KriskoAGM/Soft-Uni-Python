def rounding(numbers):
    empty_list = []
    for x in numbers:
        empty_list.append(round(x))
    return empty_list


numbers_to_round = input().split(" ")
new_list = []
for n in numbers_to_round:
    new_list.append(float(n))

print(rounding(new_list))

