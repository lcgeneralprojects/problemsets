class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        convert1 = convert2 = 0

        for i in range(len(num1)):
            convert1 = int(num1[i]) + 10 * convert1

        for i in range(len(num2)):
            convert2 = int(num2[i]) + 10 * convert2

        return str(convert1 * convert2)
    