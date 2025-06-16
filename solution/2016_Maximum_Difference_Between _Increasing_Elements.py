class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_diff = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (nums[i] < nums[j]):
                    list_diff.append(nums[j] - nums[i])
        if len(list_diff)==0:
            return -1
        else :
            list_diff.sort(reverse=True)
            print(list_diff)
            result = list_diff[0]
            #print(result)
            return result
        

obj = Solution()
print(obj.maximumDifference([7,1,5,4]))  # Output: 4
print(obj.maximumDifference([9,4,7,2,10]))  # Output: 6
print(obj.maximumDifference([1,5,2]))  # Output: 4
print(obj.maximumDifference([1,1,1]))  # Output: -1
print(obj.maximumDifference([1,2,3,4]))  # Output: 3