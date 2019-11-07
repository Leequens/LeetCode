class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s :
            if char in mapping :
                top = stack.pop() if stack else '#'
                #如果stack为空则随便赋值，使得下面判断不等返回False
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack