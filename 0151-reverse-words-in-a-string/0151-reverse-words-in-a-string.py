class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.strip()
        print(s)
        words = s.split()
        print(s)
        reversed_word = words[:: -1]
        print(reversed_word)
        return ' '.join(reversed_word) 