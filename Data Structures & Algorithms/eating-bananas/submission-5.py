from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        higher = max(piles)
        time = 0
        
        k = (lower + higher) // 2
        
        while lower <= higher:
            time = 0
            rate = (lower + higher) // 2
            for i in range(len(piles)):
                time += ceil(piles[i] / rate)
                if time > h:
                    break
            if time <= h:
                k = rate
            
            if time > h:
                lower = rate + 1
            else:
                higher = rate - 1

        return k