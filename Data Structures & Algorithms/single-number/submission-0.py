class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = Counter(nums)

        for i, n in hm.items():
            if n > 1: continue
            if n == 1: return i
