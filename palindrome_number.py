class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        copy = x
        y = 0

        while copy > 0:
            y = y * 10 + copy % 10
            copy //= 10
        
        return x == y

