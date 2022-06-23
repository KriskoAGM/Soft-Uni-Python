some_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_string = [x for x in some_string if x.lower() not in vowels]
print(''.join(new_string))


# some_string = input()
# vowels = ['a', 'o', 'u', 'e', 'i']
# final_list = []
#
# for element in some_string:
#     if element.lower() not in vowels:
#         final_list.append(element)
#
# print(*final_list, sep="")
