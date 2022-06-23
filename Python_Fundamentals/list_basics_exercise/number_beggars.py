numbers = input().split(", ")
beggars = int(input())
new_list = []
final_list = []
index_counter = 0

for element in numbers:
    new_list.append(int(element))
while True:
    beggars_sum = 0
    for index in range(index_counter, len(new_list), beggars):
        beggars_sum += new_list[index]
    index_counter += 1
    if index_counter > beggars:
        break
    final_list.append(beggars_sum)
print(final_list)


# numbers = list(map(int, input().split(", ")))
# beggars = int(input())
# list_sum = []
#
# for index in range(beggars):
#     collected = []
#     for current_index in range(index, len(numbers), beggars):
#         collected.append(numbers[current_index])
#     list_sum.append(sum(collected))
#
# print(list_sum)



