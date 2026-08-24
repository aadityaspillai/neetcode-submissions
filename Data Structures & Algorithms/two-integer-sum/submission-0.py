class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            ideal_value = target - n
            if ideal_value in hm:
                return[hm[ideal_value], i]
            hm[n] = i
            
                