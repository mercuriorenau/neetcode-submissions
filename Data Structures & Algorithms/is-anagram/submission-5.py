class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1 
        for letter in t:
            counter[letter] = counter.get(letter, 0) - 1 

        return all(v == 0 for v in counter.values()) 