class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_clean = []
        for i in s:
            if i.isalnum():
                s_clean.append(i)

        i = 0
        j = len(s_clean)-1
        while i<j:
            if s_clean[i] != s_clean[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

        # # s = s.lower()
        # # s1 = ""
        # # for i in s:
        # #     if i.isalnum():
        # #         s1 += i

        # # s_rev = s1[::-1]
        # # if s1 == s_rev:
        # #     return True
        # # else:
        #     return False
        