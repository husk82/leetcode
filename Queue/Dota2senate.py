from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i in range (n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            print(radiant, " + ", dire)
            if radiant.popleft() < dire.popleft():
                radiant.append(n)   
                n += 1
            else:
                dire.append(n)
                n += 1
            print(radiant, " - ", dire)
        return "Radiant" if radiant else "Dire" 
    
sol = Solution()

print(sol.predictPartyVictory("DRRD"))

        
