n = input().split()
inverted_list = []

for digit in n:
    digit = -int(digit)
    inverted_list.append(digit)
print(inverted_list)


# Second solution
# numbers = list(map(int, input().split()))
# inverted_list = [-x for x in numbers]
# print(inverted_list)
