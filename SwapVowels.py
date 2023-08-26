'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:

        l = 0
        r = len(s) - 1
        s = list(s)
        while (r > l):
            if s[l].lower() not in 'aeiou':
                l += 1
            elif s[r].lower() not in 'aeiou':
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)
