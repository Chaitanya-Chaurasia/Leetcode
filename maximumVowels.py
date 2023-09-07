class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        l, vowelCount, maxCount = 0, 0, 0


        for r in range(0, len(s)):
            
            if r + 1 - l > k :
                if s[l] in vowels:
                    vowelCount -= 1
                l += 1

            if s[r] in vowels:
                vowelCount += 1
                maxCount = max(maxCount, vowelCount)

        return maxCount 

        return v
