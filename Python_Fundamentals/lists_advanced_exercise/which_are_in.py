first_string = input().split(", ")
second_string = input().split(", ")
result = []

for word in first_string:
    for element in second_string:
        if word in element:
            result.append(word)
        if word in result:
            break

print(result)