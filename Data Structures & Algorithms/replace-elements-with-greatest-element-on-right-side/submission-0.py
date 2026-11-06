class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = arr[len(arr) - 1]
        temp = biggest
        arr[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > biggest:
                biggest = arr[i]
                arr[i] = temp
                temp = biggest
            else:
                arr[i] = temp
        return arr