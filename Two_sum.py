class Solution(object):
    def twoSum(self, nums, target):
        prev_map = dict()

        for i,num in enumerate(nums):
            if target - num in prev_map:
                return [i,prev_map[target-num]]
            prev_map[num] = i
        return -1    
            
solution=Solution()

nums=[2,7,11,15]
target = 13
result = solution.twoSum(nums,target)
print(result)

