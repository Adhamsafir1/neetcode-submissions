class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { '}' : '{' , ']' : '[' , ')':'('}

        for i in s:
            if i in dic:
                if stack:
                    a = stack.pop()
                    if dic[i] != a:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True