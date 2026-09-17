class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in  strs:
            alph = [0] * 26

            for letter in s.strip().lower():
                order = ord(letter) - ord('a')
                alph[order] = alph[order] + 1      
            signature = tuple(alph)
            m[signature] = m.get(signature, []) + [s]

        return list(m.values())