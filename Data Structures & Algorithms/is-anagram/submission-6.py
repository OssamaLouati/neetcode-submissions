class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1

        map_t = {}
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1
        
        if len(map_s.keys()) != len(map_t.keys()):
            return False

        for char in s:
            if map_s.get(char) != map_t.get(char, 0):
                return False
        return True