def two_sum(nums: list[int], target: int) -> list[int]:
    #* Edge cases
    if nums == [] or len(nums) < 2:
        return
    
    #* code
    seen = {}
    for idx ,val in enumerate(nums):
        if target-val in seen:
            return [idx,seen[target-val]]
        else:
            seen[val] = idx
    