some_string = input()
nums = ''
letters = ''
other = ''

for element in some_string:
    if element.isdigit():
        nums += element
    elif element.isalpha():
        letters += element
    else:
        other += element

print(nums)
print(letters)
print(other)