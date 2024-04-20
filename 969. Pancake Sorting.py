class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        increasing = True
        result = []
        right = len(arr)
        maxUnsorted = max(arr)
        unsorted = arr
        def helper(list1):
            for i in range(1, len(list1)):
                if list1[i - 1] > list1[i]:
                    return False
            return True


        while unsorted and right > 0:
            if not helper(unsorted):
                idx = unsorted.index(maxUnsorted)
                if idx >= right / 2 or idx == 0:
                    result.append(right)
                    unsorted = unsorted[::-1]
                    if maxUnsorted == unsorted[-1]:
                        unsorted = unsorted[:-1]
                        maxUnsorted = max(unsorted)
                        right -= 1
                else:
                    result.append(idx + 1)
                    unsorted = unsorted[:idx + 1][::-1] + unsorted[idx + 1:]
            else:
                break

        
        return result
            
