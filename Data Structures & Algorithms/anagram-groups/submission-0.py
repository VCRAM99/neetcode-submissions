class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = [0]*26
        anagrams = defaultdict(list)
        
        for word in strs:
            for letter in word:
                lindex = ord(letter.lower()) - ord('a') 
                letters[lindex] = 1 + letters[lindex] 
            anagrams[tuple(letters)].append(word)
            letters = [0]*26
        
        return list(anagrams.values())
            