number = int(input())

negative_list = []
positive_list = []
even_list = []
odd_list = []

for i in range(number):
    numbers = int(input())

    if numbers < 0:
        negative_list.append(numbers)
    if numbers >= 0:
        positive_list.append(numbers)
    if numbers % 2 == 0:
        even_list.append(numbers)
    if numbers % 2 != 0:
        odd_list.append(numbers)

command = input()

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)