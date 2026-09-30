class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        while len(nums) > 1:
            
            

            Len = len(nums)//2
            if nums[Len] == target:
                return True
            elif nums[Len] > target:
                nums = nums[Len:-1]
            elif nums[Len] < target:
                nums = nums[0:Len]
        return False
            
            

# temp = [1,3,5,6]
# temp_len = len(temp)//2
# temp = temp[0:temp_len]
# print(temp)



k = Solution.searchInsert([1,3,5,6],9)
print(k)