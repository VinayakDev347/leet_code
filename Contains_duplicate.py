class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False
    

solution=Solution()                 # Create an instance of the Solution class

nums = [1,2,3,1]
result = solution.containsDuplicate(nums)
print(result)