class Solution:
    def sortArray(self, nums):
        n = len(nums)

        for i in range(0,n):
            min_index = i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j

            temp = nums[min_index]
            nums[min_index] = nums[i]
            nums[i] = temp
        return nums

print(Solution().sortArray([2,3,5,3,8,5]))