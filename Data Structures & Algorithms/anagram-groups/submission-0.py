class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Stext = ""
        ans = defaultdict(list)

        for txt in strs:
            Stext = ''.join(sorted(txt))
            ans[Stext].append(txt)
        
        return list(ans.values())