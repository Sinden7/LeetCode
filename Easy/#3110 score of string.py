class Solution(object):
    def scoreOfString(self, s):
        length = len(s)
        total = 0
        for i in range(0,length-1):
                first = (ord(s[i]))
                second = (ord(s[i+1]))
                sum = (first - second)
                
                if sum < 0:
                    sum = -(sum)
                    total += sum
                else:
                    total += sum
        return total 
    
    s = "hello"
