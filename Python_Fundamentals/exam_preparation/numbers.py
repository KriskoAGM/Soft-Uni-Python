numbers = list(map(int, input().split()))
average_number = sum(numbers) / len(numbers)
top_5_list = []

for number in sorted(numbers, reverse=True):

    if number > average_number and len(top_5_list) < 5:
        top_5_list.append(number)

if top_5_list:
    print(*top_5_list)
else:
    print("No")