def find_max(nums:list[int]) -> int:
    Max = nums[0]
    index = None
    for idx ,num in enumerate(nums):
        if num > Max:
            Max = num
            index =  idx
    return index


def second_max(nums:list[int]) -> int:
    Max = nums[0]
    prev = None
    for num in nums:
        if num > Max:
            prev = Max
            Max = num
        if (prev is None or num > prev) and num < Max:
            prev = num
    return prev

k = second_max([12, 7, 25, 3, 18])
print(k)

print(second_max([5, 5, 4]))  # Expected: 4