class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        matrix = []
        for x in range(N):
            list1 = [0 for x in range(N)]
            matrix.append(list1)

        for x in trust:
            matrix[x[0]-1][x[1]-1] = 1

        # Counter for holding how many people dont trust anyone
        numOfJudges = 0
        counter = 0
        judge = 0
        for x in matrix:
            if 1 in x:
                print("",end = "") #do nothing
            else: # Add number of judges
                numOfJudges += 1
                judge = counter
                if numOfJudges > 1:
                    return -1 # Too many possible judges
            counter += 1

        #check if more than one person that trusts no one (more than one possible judge)
        if numOfJudges == 0:
            return -1 # No possible judges present in the town.
        else: # Check the column at that judge location for all ones EXCEPT judge location
            isJudge = True
            for x in range(0,N):
                if x != judge:
                    if matrix[x][judge] == 0:
                        isJudge = False
        if isJudge == True:
            return (judge+1)
        else:
            return -1 #if no judge present in the town.