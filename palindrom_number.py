class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)  # int to str 
        if s == s[::-1]:
            return True

s = Solution()
x = 121
result = s.isPalindrome(x)
print(result)