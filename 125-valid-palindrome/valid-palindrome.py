class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]',"",s)
        s=s.lower()
        s_reverse = s[::-1]
        s_reverse = s_reverse.lower()
        if s == s_reverse:
            return True
        else:
            return False

        