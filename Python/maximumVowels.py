class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # just like maxAvg problem

        current_count = 0
        
        for i in range(k):
            if s[i] in "aeiou":
                current_count += 1
            
        max_count = current_count

        for i in range(k, len(s)):
            print(i, k)
            if s[i - k] in "aeiou":
                current_count -= 1
            if s[i] in "aeiou":
                current_count += 1
            if current_count > max_count:
                max_count = current_count
        
        return max_count
