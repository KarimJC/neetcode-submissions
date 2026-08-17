class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tdict = {}
        for char in t:
            if char in tdict:
                tdict[char] += 1
            else:
                tdict[char] = 1

        for letter in s:
            if letter not in tdict:
                return False
            
            if tdict[letter] == 1:
                tdict.pop(letter)
            else:
                tdict[letter] -= 1
        
        if tdict:
            return False
        else:
            return True
            
