class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = list(range(numRows)) + list(range(numRows  -2 ,0,-1))
        r = [''] * numRows
        for i , char in enumerate(s):
            r[t[i%len(t)]] += char
        return "".join(r)