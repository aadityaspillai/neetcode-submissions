class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in pairs:

                if not stack:
                    return False

                most_recent = stack.pop()

                if most_recent != pairs[char]:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0