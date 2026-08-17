from collections import Counter

class Solution:
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramHash = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in anagramHash:
                anagramHash[sortedWord].append(word)
            else:
                anagramHash[sortedWord] = [word]

        return list(anagramHash.values())