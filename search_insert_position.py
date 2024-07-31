# 35. Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while right >= left:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
        
solution = Solution()
nums = [1,3,5,6]
target = 5
result = solution.searchInsert(nums,target)
print(result)