class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeros, ones = 0, 0

        for num in students:
            if num == 0:
                zeros += 1
            else:
                ones += 1
        
        for num in sandwiches:
            if num == 0 and zeros > 0:
                zeros -= 1
            elif num == 0 and zeros == 0:
                return ones
            elif num == 1 and ones > 0:
                ones -= 1
            else:
                return zeros 

        return 0
