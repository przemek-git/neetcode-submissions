class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums=[-1,0,3,5,9,12] target = 5 len = 6  5 // 2 = 2.5 - 2
        # nums=[-1,0,3,5,9] target = 5 len = 5     4 // 2 = 2 - 2
        
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