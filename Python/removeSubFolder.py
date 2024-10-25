class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # since each folder name is unique, if not a subfolder, it will start with a different alphabet
        # in this case, we can sort the list, so all the subfolders will be arranged adjacently.
        # we simply iterate the list and check fora subfolder condition

        if len(folder) == 1:
            return folder
        folder.sort()
        res = [folder[0]]
        prev = folder[0]
        for i in range(1, len(folder)):
            if not folder[i].startswith(prev + "/"):
                res.append(folder[i])
                prev = folder[i]
        return res
