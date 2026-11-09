class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_length = 0

        for char in s:
            if char in substring:
                # Remove characters from the start until we remove the repeated one
                substring = substring[substring.index(char) + 1:]
            substring += char
            max_length = max(max_length, len(substring))

        return max_length