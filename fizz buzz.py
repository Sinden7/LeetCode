class Solution(object):
    def fizzBuzz(self, n):
        numbers = []
        for i in range(1,n+1):
            if i % 3 == 0 and int(i) % 5 == 0:
                numbers.append("FizzBuzz")
        
            elif i % 3 == 0:
                numbers.append("Fizz")
        
            elif i % 5 == 0:
                numbers.append("Buzz")

            else:
                numbers.append(str(i))  
                
        return(numbers)
    
    n = 3
    