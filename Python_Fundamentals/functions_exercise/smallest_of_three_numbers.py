def smallest(a, b, c):
    new_list = [a, b, c]
    return min(new_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest(first_number, second_number, third_number))
