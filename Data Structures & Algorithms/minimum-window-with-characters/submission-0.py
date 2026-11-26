class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        minim = float("inf")
        left = 0
        ramase = len(t)
        rezultat = (0, 0)

        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        for right in range(len(s)):
            c = s[right]
            if c in freq_t:
                if freq_t[c] > 0:
                    ramase -= 1
                freq_t[c] -= 1

            while ramase == 0:
                minim_right = right - left + 1
                if minim_right < minim:
                    minim = minim_right
                    rezultat = (left, right)

                if s[left] in freq_t:
                    freq_t[s[left]] += 1
                    if freq_t[s[left]] > 0:
                        ramase += 1
                left += 1

        if minim != float("inf"):
            return s[rezultat[0] : rezultat[1] + 1]
        else:
            return ""