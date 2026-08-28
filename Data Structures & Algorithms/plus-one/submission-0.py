class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_value = len(digits) - 1
        i = last_value

        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits          # no carry, done
            digits[i] = 0              # 9 -> 0, carry left
            i -= 1                # chop it off
         
        return [1] + digits