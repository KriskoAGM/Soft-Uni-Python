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



