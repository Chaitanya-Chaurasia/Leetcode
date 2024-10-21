class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # logic is as follows:
        # we start by iterating through every digit in the digits string.
        # for each digit, we iterate through its letters in keyboard.
        # we do this recursively and increment the idx by 1 to keep track of when all the digits have been traversed to 
        # find a mapping.
        # we repeat this in a for loop.

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

        def backtrack(idx, combination):
            if idx == len(digits):
                mappings.append(combination)
                return
            
            curr_digit = digits[idx]
            
            for i in keyboard[curr_digit]:
                backtrack(idx + 1, combination + i)
        
        mappings = []
        backtrack(0, "")
        return mappings
