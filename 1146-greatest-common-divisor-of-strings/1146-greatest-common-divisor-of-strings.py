from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:  # If they can't be constructed from a common substring
            return ""
        
        gcd_length = gcd(len(str1), len(str2))
        print(gcd_length)
        return str1[:gcd_length]  # The common divisor substring


        