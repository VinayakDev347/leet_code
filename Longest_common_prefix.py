class Solution(object):
    def longestCommonPrefix(self, strs):
        res=""

        for i in range(len(strs[0])):
            for s in strs:        
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res+=strs[0][i]

        return res
    

solution  = Solution()
strs = ["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print(result)