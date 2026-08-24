class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)      # {1:1, 2:2, 3:3}
        result = []

        for i in range(k):          # do the search k times
            best_num = None
            best_count = -1
            for num, cnt in counts.items():
                if cnt > best_count:
                    best_count = cnt
                    best_num = num
            result.append(best_num)
            del counts[best_num]    # exclude it from the next pass

        return result