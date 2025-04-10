class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digitLogs, letterLogs = [], []

        def isDigitLogs(log):
            if log.split()[1] and log.split()[1].isdigit():
                return True
            return False
        
        def sortLetterLogs():
            # we use maxSplit parameter to get the identifier, and the start of the logs.
            # We sort then based on priority of logs first, then identifier.
            return letterLogs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        for i in logs:
            if isDigitLogs(i):
                digitLogs.append(i)
            else:
                letterLogs.append(i)
        
        sortLetterLogs()

        return letterLogs + digitLogs
