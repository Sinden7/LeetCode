class Solution(object):
    def reverseDegree(self, s):
        reversed_alphabet = ["z", "y", "x","w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a",]

        sum = 0
        
        for index, letter in enumerate(s):
            reversed_index = reversed_alphabet.index(letter)
            #Adding 1 since python starts counting from 0    
            product = ((index)+1) * ((reversed_index)+1)  
            sum += product

        return(sum)

        