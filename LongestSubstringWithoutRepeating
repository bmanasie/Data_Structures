class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        list = []
        maxCount = 0
        start = 0
        
        for ind,char in enumerate(s):
            
            if char in s[start:ind]:
                
                list.append(char)
                lengthString = ind - start
                maxCount = max(lengthString,maxCount)
                start = list.index(char, start, ind) +  1
                
                    
            else:
                
                list.append(char)
        
        lengthString = len(list) - start
        maxCount = max(lengthString,maxCount)
        return maxCount
                
                
