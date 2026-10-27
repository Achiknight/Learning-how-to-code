def remove_duplicates(nums: list[int]) -> int:
    if nums == []:
        return 0
    uniqe = 1
    for index in range(1,len(nums)):
        last = index-1
        if nums[index] == nums[last]:
            pass
        else:
            nums[uniqe] = nums[index]
            uniqe+=1

    return uniqe
            
            
            
            
            
            
            
            
            
# * [1,1,2,3,3]
#* idx = 0 last = -1  False k+=1    k = 1
#* idx = 1 last = 0   True pop last append idx   
#? new = [1,2,3,3,1]
#* idx = 2 last = 1 False k+=1   k = 2 
#* idx = 3 last = 2 True pop last append idx
#? new = [1,2,3,1,3] 
#* idx = 4 last =3 false






nums = []
k = remove_duplicates(nums)
print(k, nums[:k])  # 0, []

nums = [7]
k = remove_duplicates(nums)
print(k, nums[:k])  # 1, [7]

nums = [2, 2, 2, 2]
k = remove_duplicates(nums)
print(k, nums[:k])  # 1, [2]

nums = [1, 1, 2, 2, 3, 3]
k = remove_duplicates(nums)
print(k, nums[:k])  # 3, [1, 2, 3]

nums = [1, 2, 3, 4]
k = remove_duplicates(nums)
print(k, nums[:k])  # 4, [1, 2, 3, 4]