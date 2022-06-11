def ascii_range(a, b):
    char_list = []
    for x in range(ord(a) + 1, ord(b)):
        char_list.append(chr(x))
    return char_list


first_char = input()
second_char = input()

result = ascii_range(first_char, second_char)
print(*result)