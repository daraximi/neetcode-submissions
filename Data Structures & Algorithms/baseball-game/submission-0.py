class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            print(operations[i])
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "D":
                temp = stack[-1]
                stack.append(2 * int(temp))
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)