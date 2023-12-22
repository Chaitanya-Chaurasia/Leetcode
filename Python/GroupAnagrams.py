from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []

        d = defaultdict(lambda: 0)

        for i in strs:

            # SORT EACH STRING
            s = "".join(sorted(i))

            # IF SORTED STRING EXISTS IN DICT, APPEND "UNSORTED STRING"
            if s in d:
                d[s].append(i)
            
            # ELSE, APPEND FIRST TIME
            else:
                d[s] = [i]
        

        for i in d:
            output.append(d[i])

        return output
