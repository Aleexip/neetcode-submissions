class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq = {}

        left=maxim = 0 
        for right in range(len(s)):
            frq[s[right]] = frq.get(s[right],0) + 1

            while (right - left + 1) - max(frq.values()) > k:
                frq[s[left]] -= 1
                left += 1

            maxim = max(maxim, right - left + 1)
        return maxim
        