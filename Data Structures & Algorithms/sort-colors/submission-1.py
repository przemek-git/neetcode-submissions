class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0] * 3 

        for n in nums:
            buckets[n] += 1

        i = 0
        for j in range(len(buckets)):
            for _ in range(buckets[j]):
                nums[i] = j
                i += 1
        