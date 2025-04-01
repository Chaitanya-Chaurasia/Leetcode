class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Our approach: Backtracking
        # In our function, with every call, we increment the index of string.
        # For every character in the string, we iterate over a hashmap of possible combinations

        if not digits:
            return []
        
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        combinations = []

        def backtrack(index, comb):
            if index == len(digits):
                combinations.append(comb)
                return
            
            for letter in keyboard[digits[index]]:
                backtrack(index + 1, comb + letter)

        backtrack(0, "")
        return combinations    
