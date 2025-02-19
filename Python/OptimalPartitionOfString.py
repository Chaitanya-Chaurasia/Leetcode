class Solution:
    def partitionString(self, s: str) -> int:

        # this is an easy question
        # simply iterate from the starting of the string.
        # maintain a hashset to store all substrings we encounter
        # at every index, check if the character was part of hashset.
        # if yes, we've found one optimal substring. update result variables accordingly
        # we will return res + 1, because at the last partition, our loop terminates without incrementing by 1.   
        res, hashset = 0, set()
        for char in s:
            if char in hashset:
                res += 1
                hashset = set()
            #     hashset.add(char)
            # else:
            #     hashset.add(char)
            # simply replace the above code by one line
            hashset.add(char)
        return res + 1
