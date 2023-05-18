class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        i = 0
        aux = 0

        if x < 0:
            return False

        while 10**i <= x:
            aux *= 10
            aux += (x % 10**(i+1)) / 10**i
            i += 1

        if aux == x:
            return True
        else:
            return False
