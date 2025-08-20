class Solution:    
    def twoSum(self,nums,target):
        dicti={}
        for i,num in enumerate((nums)):
            complement=target-num
            if complement in dicti:
                return [dicti[complement],i]
            dicti[num]=i
