while True:
    string = input()

    if string == 'End':
        break
    elif string == 'SoftUni':
        continue

    double_char = "".join([x * 2 for x in string])
    print(double_char)


