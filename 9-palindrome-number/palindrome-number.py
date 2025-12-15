class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        list=[]
        while(x!=0):
            rem=x%10
            x=x//10
            list.append(rem)

        return True if (list==list[::-1]) else False 