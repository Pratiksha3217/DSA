class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i

        s_rev = s1[::-1]
        if s1 == s_rev:
            return True
        else:
            return False
        