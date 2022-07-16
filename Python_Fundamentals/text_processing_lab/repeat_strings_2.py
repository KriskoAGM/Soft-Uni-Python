strings = input().split()
final_string = ''

for word in strings:
    final_string += word * len(word)

print(final_string)