class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        theSame = (sorted(s) == sorted(t))
        if  not theSame: 
            return False
        return True
        