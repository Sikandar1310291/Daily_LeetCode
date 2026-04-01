import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        total = 0
        last_d = 0
        if x < 0:
            return False
        while x > 0:
            last_d = x % 10
            total = (total * 10) + last_d
            x = x//10
        if total == num :
            return True
        else :
            return False