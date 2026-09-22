class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            num = x
            reversed_num = 0

            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10

            if reversed_num == x:
                return True
        
            else:
                return False


    x = 121
