def positive(nums):
    result = [x for x in nums if int(x) >= 0]
    return ", ".join(result)


def negative(nums):
    result = [x for x in nums if int(x) < 0]
    return ", ".join(result)


def even(nums):
    result = [x for x in nums if int(x) % 2 == 0]
    return ", ".join(result)


def odd(nums):
    result = [x for x in nums if int(x) % 2 != 0]
    return ", ".join(result)


numbers = input().split(", ")

print(f"Positive: {positive(numbers)}")
print(f"Negative: {negative(numbers)}")
print(f"Even: {even(numbers)}")
print(f"Odd: {odd(numbers)}")


