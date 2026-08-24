class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        starting_num = nums[0]
        consecutive = 0
        highest_consecutive = 0

        for num in nums:
            difference = num - starting_num
            if difference == 0:
                starting_num = num
            if difference > 1:
                starting_num = num
                consecutive = 0
            if difference == 1:
                consecutive += 1
                starting_num = num
                if consecutive > highest_consecutive:
                    highest_consecutive = consecutive
        return highest_consecutive + 1
            