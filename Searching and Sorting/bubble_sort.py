class Solution:
    def sortArray(self, nums):
        n = len(nums)

        for i in range(n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    isSwap = True

            if not isSwap:
                break

        return nums

a = Solution()
nums = [2,3,5,3,8,5]
print(a.sortArray(nums))