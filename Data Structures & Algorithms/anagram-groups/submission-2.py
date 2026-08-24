from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            hash = str(sorted(s))
            group[hash].append(s)
        return list(group.values())