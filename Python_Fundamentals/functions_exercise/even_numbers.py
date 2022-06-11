# function to chek if a number is even
def even_number(number):
    if num % 2 == 0:
        return True
    return False


# list comprehension to create an integer list from user input
numbers = [int(x) for x in input().split()]

even_list = []
for num in numbers:
    if even_number(num):  # checking if the number in the list is even with the function we created
        even_list.append(num)
print(even_list)
