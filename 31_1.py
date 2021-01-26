class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #m1 1/25/2021
        def reverse(low: int, high: int):
            i, j = low, high
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        size = len(nums)
        if size < 2:
            return
        found = False
        i = size - 2
        while i >= 0:
            j = size - 1
            while j > i:
                if nums[j] > nums[i]:
                    nums[j],nums[i] = nums[i], nums[j]
                    reverse(i + 1, size - 1)
                    return
                j -= 1
            i -= 1
        i, j = 0, size - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
