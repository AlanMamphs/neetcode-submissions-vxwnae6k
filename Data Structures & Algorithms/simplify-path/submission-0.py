class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        last = ''
        for p in path + '/':
            if p == '/':
                if last == '.':
                    pass
                elif last == '..':
                    if stack:
                        stack.pop()
                elif last:
                    stack.append(last)
                last = ''
            else:
                last += p
        return '/' + '/'.join(stack)
                
               
