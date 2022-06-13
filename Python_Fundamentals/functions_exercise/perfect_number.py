def perfect_number(number):
    sum = 0
    for div in range(1, number):
        if number % div == 0:
            sum += div
    if number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())
print(perfect_number(num))
