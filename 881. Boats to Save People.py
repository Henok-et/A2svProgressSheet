class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        cnt = 0
        left , right = 0, n-1
        while left <= right :
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                cnt += 1

            else :
                right -= 1
                cnt += 1
        
        return cnt
