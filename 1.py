class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #m0 01162021
        visited = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in visited and visited[c] != i:
                return sorted([visited[c], i])
            visited[n] = i
        return None
