def palindrome(words):
    return words[::-1]


string = input().split()
searching_word = input()
result = []

for word in string:
    palindrome_word = palindrome(word)
    if word == palindrome_word:
        result.append(word)

print(result)
print(f"Found palindrome {result.count(searching_word)} times")

