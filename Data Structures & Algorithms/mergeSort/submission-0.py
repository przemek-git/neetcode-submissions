# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
            if len(pairs) <= 1:
                return pairs
            
            half = len(pairs) // 2
            left = self.mergeSort(pairs[:half])
            right = self.mergeSort(pairs[half:])

            merged = []

            l, r = 0, 0

            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            while l < len(left):
                merged.append(left[l])
                l += 1

            while r < len(right):
                merged.append(right[r])
                r += 1

            return merged
        
            