class Solution(object):

    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]

            seen[num] = i

nums = [2,4,6,2,8]
target = 8
a = Solution()
print(a.twoSum(nums,target))