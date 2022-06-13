def palindrome(n):
    return n[::-1]


nums = [int(x) for x in input().split(", ")]

for num in nums:
    number = palindrome(str(num))
    if int(number) == num:
        print("True")
    else:
        print("False")
