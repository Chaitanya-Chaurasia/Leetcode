class Solution:
    def compress(self, chars: List[str]) -> int:

        self.s = ""

        for i in chars:
            if chars.count(i) == 1 and i not in self.s:
                self.s += (i + "#" + str(chars.count(i)) + "#")

                if chars.count(i) > 1 and i not in self.s:
                        if (chars.count(i) >= 10):
                            self.s += (i + "#" + str(chars.count(i))[0] + "#" + str(chars.count(i))[1] + "#")
                        else:
                            self.s += (i + "#" + str(chars.count(i)) + "#")

        

        chars = (self.s).split("#")
        del chars[-1]

        print(chars)
        return len(chars)
                

