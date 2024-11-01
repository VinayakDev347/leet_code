class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

solution=Solution()                 # Create an instance of the Solution class

nums = [1,2,3,1]
result = solution.containsDuplicate(nums)
print(result)                                     #True 
