def group(nums):
    boundary = 0

    while len(nums) > 0:
        empty_list = []
        boundary += 10
        for num in nums:
            if num <= boundary:
                empty_list.append(num)
        print(f"Group of {boundary}'s: {empty_list}")
        nums = [x for x in nums if x not in empty_list]


numbers = list(map(int, input().split(", ")))
group(numbers)
