class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for stre in s:
                count[ord(stre) - ord('a')] += 1
            maps[tuple(count)].append(s)
        return list(maps.values())