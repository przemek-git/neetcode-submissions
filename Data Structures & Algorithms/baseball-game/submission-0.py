class Solution:
    

    def calPoints(self, operations: List[str]) -> int:
        stack = [0] * len(operations)
        tail = 0;
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    stack[tail] = stack[tail - 1] + stack [tail - 2]
                    tail += 1
                case "C":
                    stack[tail - 1] = 0
                    tail -= 1
                case "D":
                    stack[tail] = stack[tail - 1] * 2
                    tail += 1
                case _:
                    stack[tail] = int(operations[i])
                    tail += 1
        return sum(stack)
