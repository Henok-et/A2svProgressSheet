class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i = 0
        j = len(nums)-1
        count = 0
        while i<j:
            t = nums[i] + nums[j]
            if t == k:
                count+=1
                i+=1
                j-=1
            elif t>k:
                j-=1
            else:
                i+=1
        return count

