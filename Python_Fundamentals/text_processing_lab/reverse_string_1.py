while True:
    words = input()

    if words == "end":
        break

    reversed_word = words[::-1]

    print(f"{words} = {reversed_word}")