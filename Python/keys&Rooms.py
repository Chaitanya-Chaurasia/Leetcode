class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # approach
        # since every element in the array is room i with keys, we need two lists:
        # one for maintaining if room i has been visited, and a stack to add key to explore

        l = len(rooms)
        visited, stack, count = [False] * l, [0], 1
        visited[0] = True

        while stack:
            current_room = stack.pop()
            for keys_found in rooms[current_room]:
                if not visited[keys_found]:
                    stack.append(keys_found)
                    visited[keys_found] = visited
                    count += 1
        return count == l
