class Solution(object):
    def maximum69Number (self, num):
       nums=str(num)
       res=nums.replace("6","9",1)
       return int(res)
        