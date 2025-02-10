class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        last_sign = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == len(s) 1:
                if last_sign == '+': stack.append(num)
                if last_sign == '-': stack.append(-num)
                if last_sign == '*': stack.append(stack.pop() * num)
                if last_sign == '/': stack.append(int(stack.pop() / num))
                last_sign = char
                num = 0
        return sum(stack)
