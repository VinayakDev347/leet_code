"""
1)
"""
# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0:
#             return False
#         s = str(x)  # int to str 
#         if s == s[::-1]:
#             return True

"""
2)
"""
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x
        rev = 0 
        while temp != 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp //= 10
        return rev == x



s = Solution()
x = 121
result = s.isPalindrome(x)
print(result)
