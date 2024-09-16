class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # for operation 1, we can just check if both words have same sort arrangements
        # for operation 2, we can just check if count of unique characters are same, given same length

        if len(word1) != len(word2):
            return False
        
        d1 = {}
        d2 = {}

        for i in word1:
            d1[i] = d1.get(i, 0) + 1
        
        for i in word2:
            d2[i] = d2.get(i, 0) + 1

        # check if alphabets are same
        if set(d1.keys()) != set(d2.keys()):
            return False
        
        # if same, check if frequency of each letter is same
        a=list(d1.values())
        b=list(d2.values())
        a.sort()
        b.sort()
        return a==b
