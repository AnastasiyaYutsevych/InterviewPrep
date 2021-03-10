def reverse(x):
    result = 0
    negative = True if x<0 else False
    x= abs(x)
    while x>0:
        if x%10!= 0 or result>0:
            result = result*10 + x%10
        x = x//10
    if result > 2**31 -1 or (-result <-2**31 and negative):
            return 0
    if negative:
        return  -result
    return result

print(reverse(1020))