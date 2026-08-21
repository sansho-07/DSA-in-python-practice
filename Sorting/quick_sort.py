class Solution:

    def partition(self,nums,l,r):
        key = nums[r]
        start = l
        for i in range(l,r+1):
            if nums[i]<=key:
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start+=1
        return start-1

    
    def quick_sort(self,nums,l,r):
        if l>=r:
            return

        p = self.partition(nums,l,r)

        self.quick_sort(nums,l,p-1)
        self.quick_sort(nums,p+1,r)


    def sortArray(self, nums):
        n = len(nums)
        self.quick_sort(nums,0,n-1)

        return nums