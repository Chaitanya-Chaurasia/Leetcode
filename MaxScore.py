class Solution:
    def maxScore(self, s: str) -> int:

        # ITERATE THROUGH THE STRING
        # COUNT THE NUMBER OF 0s ON THE LEFT 
        # COUNT THE NUMBER OF 1s ON THE RIGHT
        # CALCULATE SCORE AND FINALLY MAX SCORE

        if "1" not in s:
            return len(s) - 1 

        max_score = 0

        for i in range(1, len(s)):

            left = s[0 : i].count("0")
            right = s[i : ].count("1")

            print(s[0: i], s[i:])
            score = left + right
            
            if score > max_score:
                max_score = score
        
        return max_score

        
