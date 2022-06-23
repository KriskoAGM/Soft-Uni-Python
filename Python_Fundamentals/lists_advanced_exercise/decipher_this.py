secret_message = input().split()
final_list = []

for word in secret_message:
    numbers = ''
    for digit in word:
        if digit.isdigit():
            numbers += digit
        else:
            break
    new_word = word.replace(numbers, chr(int(numbers)))
    if len(new_word) >= 3:
        new_word = new_word[0] + new_word[-1] + new_word[2:-1] + new_word[1]
    final_list.append(new_word)
print(*final_list)








