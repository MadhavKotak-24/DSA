class Solution(object):
    def isValid(self, s):
       
        
        stack=[]
        dict={"]":"[","}":"{",")":"("}
        for char in s:
            if char in dict:
                stack_top=stack.pop() if stack else "#"
                if dict[char]!=stack_top:
                    return False
            else:
                stack.append(char)
        return not stack