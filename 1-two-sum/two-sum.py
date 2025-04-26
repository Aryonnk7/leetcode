class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], idx]
            num_dict[num] = idx