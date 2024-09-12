class Solution:
    def compress(self, chars: List[str]) -> int:

        # iterate and check where a new group of characters start.
        # store the index, and just add the count in a new array.
        # modify existing list into a new list.

        i = 0
        write_index = 0

        while (i < len(chars)):
            
            current_char = chars[i]
            # get the count of current character in chars array
            count = 0

            while (i < len(chars) and chars[i] == current_char):
                i += 1
                count += 1
            
            # now, calculate the write_index. 
            chars[write_index] = current_char
            write_index += 1

            # if count is more than 1 digit, parse through the number as a string and add it at write_index
            if count > 1:
                for j in str(count):
                    chars[write_index] = j
                    write_index += 1

        return write_index
        
