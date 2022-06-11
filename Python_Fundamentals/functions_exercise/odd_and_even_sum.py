def even_sum(number):
    even_list = []
    for x in number:
        if int(x) % 2 == 0:
            even_list.append(int(x))
    return sum(even_list)


def odd_sum(number):
    odd_list = []
    for x in number:
        if int(x) % 2 != 0:
            odd_list.append(int(x))
    return sum(odd_list)


num = input()

sum_of_even_digits = even_sum(num)
sum_of_odd_digits = odd_sum(num)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
