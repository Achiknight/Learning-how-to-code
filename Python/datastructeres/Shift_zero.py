def shift_zero(nums:list[int]) -> list[int]:
    if 0 not in nums:
        return nums
    
    write = 0
    
    for idx in range(len(nums)):
        if nums[idx] != 0:
            nums[write] = nums[idx]
            write += 1
    popper = -1
    
    k = len(nums)- write
    while k > 0:
        nums.pop(popper)
        nums.append(0)
        k -= 1
        popper -=1
    
    return nums
#! [0,1,0,3,12]


print(shift_zero([0, 1]))        # Expected: [1, 0]
print(shift_zero([0, 1, 0]))     # Expected: [1, 0, 0]









print(shift_zero([0, 1, 2]))     # Expected: [1, 2, 0]
print(shift_zero([1, 0, 2]))     # Expected: [1, 2, 0]