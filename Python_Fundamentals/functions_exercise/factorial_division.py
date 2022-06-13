def calculate_factorial(num):
    for fac in range(1, num):
        num *= fac
    return num


first_num = int(input())
second_num = int(input())

first_factorial = calculate_factorial(first_num)
second_factorial = calculate_factorial(second_num)
result = first_factorial / second_factorial
print(f"{result:.2f}")
