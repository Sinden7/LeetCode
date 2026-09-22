class Solution(object):
    def findWordsContaining(self, words, x):
        
        array = []
        
        for index, word in enumerate(words):
            if x in word:
                array.append(index)
                continue
            
            else:
                continue

        return(array)

