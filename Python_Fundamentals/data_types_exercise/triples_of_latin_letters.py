number = int(input())

for first_letter in range(0, number):
    for second_letter in range(0, number):
        for third_letter in range(0, number):
            print(f"{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}")
            