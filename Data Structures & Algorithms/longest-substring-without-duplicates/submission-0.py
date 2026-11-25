class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()

        left=maxim = 0

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])

            length = right-left + 1
            maxim = max(maxim,length)

        return maxim



