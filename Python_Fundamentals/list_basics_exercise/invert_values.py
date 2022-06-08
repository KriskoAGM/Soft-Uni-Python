n = input().split()
inverted_list = []

for digit in n:
    digit = -int(digit)
    inverted_list.append(digit)
print(inverted_list)