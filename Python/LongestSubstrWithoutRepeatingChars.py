class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Our approach: Two Pointers + Set (to keep track of repeating characters)

        left = 0
        ans = 0
        chars = set()

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            ans = max(ans, right - left + 1)
        print(chars)
        return ans
