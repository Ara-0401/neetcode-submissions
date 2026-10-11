class Solution:
    def simplifyPath(self, path: str) -> str:
        lst=path.split("/")
        stack=[]

        for directory in lst:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory!="" and directory !=".":
                stack.append(directory)
        return "/"+"/".join(stack)
        