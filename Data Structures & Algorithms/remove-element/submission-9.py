class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [r,l,r,r,r,r,r,l,l,l,r] val = r
        #  p2r
        # [  l] p2r = l p2r++
        ptr, k = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                ptr += 1
            else:
                k += 1
        print(nums, k)
        return ptr
