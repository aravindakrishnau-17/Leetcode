class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return []
        """
        """
        for i in range(len(numbers)):
            l,r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1,mid+1]
                elif numbers[mid] >tmp:
                    r=mid - 1
                else:
                    l=mid + 1
        return []
        """
        """
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i+1]
            mp[numbers[i]] = i + 1
        return []
        """
        l,r = 0, len(numbers)- 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if target < curSum:
                r -= 1
            elif target > curSum:
                l += 1
            else:
                return [l+1 , r+1]
        return []
            
        