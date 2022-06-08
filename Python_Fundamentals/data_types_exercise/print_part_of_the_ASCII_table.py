start_point = int(input())
end_point = int(input())
chars = ''

for number in range(start_point, end_point + 1):
    chars += chr(number) + " "

print(chars)
