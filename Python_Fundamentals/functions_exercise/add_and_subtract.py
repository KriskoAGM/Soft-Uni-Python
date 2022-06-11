def sum_numbers(first, second):
    return first + second


def subtract(sum_number, third):
    return sum_number - third


def add_and_subtract(first, second, third):
    sum_of_numbers = sum_numbers(first_number, second_number)
    return subtract(sum_of_numbers, third_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
