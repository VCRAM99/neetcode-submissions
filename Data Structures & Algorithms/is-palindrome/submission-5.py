class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for x in s:
            if x.isalnum():
                cleaned = cleaned + x.lower()
        
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False