class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Stext = ""
        hash_s = defaultdict(list)

        for string in strs:
            Stext = ''.join(sorted(string))
            hash_s[Stext].append(string)
        
        return list(hash_s.values())