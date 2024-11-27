class Solution(object):
    def interpret(self, command):
        return command.replace("()","o").replace("(al)","al")
        

command = "G()(al)"
# command = "G()()()()(al)"
# command = "(al)G(al)()()G"
sol = Solution()
result = sol.interpret(command)
print(result)