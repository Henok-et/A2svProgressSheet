class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {} 
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = [i, i]
            else:
                mp[s[i]][1] = i
        vals = sorted(mp.values(), key = lambda x : x[1]) # first, last occurances list sorted by last occurances
        ans, start, end = [], vals[-1][0], vals[-1][1] 
        for i in range(len(vals)-2, -1, -1):
            sx, ex = vals[i]
            if ex  > start:
                start = min(sx, start)
            else:
                ans.append(end - start + 1)
                start, end = sx, ex
        ans.append(end - start + 1)
        return ans[::-1]
        
