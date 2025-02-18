class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s

        # our approach is to expand on left and right side of every index in the string
        # expansion will keep on occuring until string remains palindrome
        # once we get the final string, we store the start and end indices of the string
        # one thing to keep in mind is that our palindrome expansion will depend upon whether string in odd or even length.
        # for an odd string, the center of palindrome must be one.
        # but for an even string, there can be possibly two centers in case the palindrome also turns out to be even length
        
        start, end = 0, 0

        def isPalindrome(l, r):
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(len(s)):
            longest = max(isPalindrome(i, i), isPalindrome(i, i + 1))
            # the length of the palindrome we get in longest will be longest.
            # hence starting index will be i - half of the length of palindrome
            # similarly, end will be i + half of the length of palindrome
            if longest > end - start:
                start = i - (longest - 1) // 2
                end = i + (longest) // 2

        return s[start: end + 1]
