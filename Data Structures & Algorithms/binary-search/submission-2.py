class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        p = len(nums) - 1

        while l <= p:
            m = (l + p) // 2 
            if nums[m] > target:
                p = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m 
        
        return -1 