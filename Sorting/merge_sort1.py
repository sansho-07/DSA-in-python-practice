class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums)<=1:
            return nums
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.merged_sort(left, right)


    def merged_sort(self,nums1,nums2):
        i = j = 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        
        while i<len(nums1):
            merged.append(nums1[i])
            i+=1
        
        while j<len(nums2):
            merged.append(nums2[j])
            j+=1
        
        return merged
