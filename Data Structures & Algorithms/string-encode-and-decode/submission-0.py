class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            tag = str(len(word)) + "#" + word
            result += tag
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            hash_position = s.find("#", i)
            word_length = int (s[i:hash_position])
            start = hash_position + 1
            end = start + word_length
            word = s[start:end]
            result.append(word)
            i=end
        return result




