class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(0,length):
            for j in range(i+1, length):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []

        nums = [2, 7, 11, 15]
        target = 9
