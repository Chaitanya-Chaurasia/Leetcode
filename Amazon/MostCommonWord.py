import re
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = defaultdict(int)
        banned_set = set(banned)
        
        words = re.findall(r"[a-z]+", paragraph.lower())
        
        for w in words:
            if w not in banned_set:
                freq[w] += 1

        return max(freq, key=freq.get)
