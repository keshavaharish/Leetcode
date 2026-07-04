class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1=[]
        nums2=[]
        for i in range(len(nums)):
            if nums[i]==0:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        nums[:]=nums2+nums1
        print(nums)

        