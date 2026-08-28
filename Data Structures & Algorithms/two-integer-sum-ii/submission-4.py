class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_num = numbers[l] + numbers[r]
            if current_num < target:
                l += 1
            if current_num > target:
                r -= 1
            if current_num == target:
                return [l + 1, r + 1]
            