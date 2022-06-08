def calculator(operator, a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b

    return result


entered_operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(entered_operator, first_number, second_number))
