class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.strip()
        print(s)
        words = s.split()
        reversed_word = words[:: -1]
        return ' '.join(reversed_word) 