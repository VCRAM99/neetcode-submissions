class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            letters = [0]*26
            for letter in word:
                lindex = ord(letter) - ord('a') 
                letters[ ord(letter) - ord('a') ] += 1
            anagrams[tuple(letters)].append(word)
        
        return list(anagrams.values())
            