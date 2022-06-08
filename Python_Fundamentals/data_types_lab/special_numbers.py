n = int(input())

for number in range(1, n + 1):
    digit_sum = 0
    digit = number

    while digit > 0:
        digit_sum += digit % 10
        digit = int(digit / 10)

    if (digit_sum == 5) or (digit_sum == 7) or (digit_sum == 11):
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
