class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in  strs:
            sorted_string = "".join(sorted(s))
            group = m.get(sorted_string, [])

            if not group:
                m[sorted_string] = [s]
            else:
                m[sorted_string] = group + [s]

        res = []
        for group in m.values():
            res.append(group)

        return res
        
