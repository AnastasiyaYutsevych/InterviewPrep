def hasMatchingParens(arr):
    if len(arr)==0:
        return True
    stack = []
    for i in arr:
        if i == '(':
            stack.append('(')
        else:
            if len(stack)== 0:
                return False
            stack.pop()
    return len(stack)== 0



# Should be true
print(hasMatchingParens("()()"))
print(hasMatchingParens("(()(()))(())"))

# Should be false
print(hasMatchingParens("()()()((()()))()(()"))
print(hasMatchingParens("()()()((())))()(()"))
