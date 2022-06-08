first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    text = str(number)

    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(text):

        if index % 2 == 0:
            odd_sum += int(digit)

        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')