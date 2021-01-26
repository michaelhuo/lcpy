class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #m0 1/25/2021
        def select_sort(low: int, high: int):
            for i in range(low, high + 1):
                m = i
                for j in range(i + 1, high + 1):
                    if nums[j] < nums[m]:
                        m = j
                if m != i:
                    nums[i], nums[m] = nums[m], nums[i]

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
                    select_sort(i + 1, size - 1)
                    return
                j -= 1
            i -= 1
        i, j = 0, size - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
