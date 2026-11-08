class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [r,l,r,r,r,r,r,l,l,l,r] val = r
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[n - 1] 
                n -= 1
        return i 