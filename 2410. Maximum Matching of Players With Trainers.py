class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        total = 0
        players.sort()
        trainers.sort()
        start = len(trainers)-1 
        for i in players[::-1]:
            if start >= 0 and i <= trainers[start]:
                start -= 1
                total +=1
        return total
