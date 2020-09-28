#Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
def plusOne(digits):
    carry= True
    i = len(digits)-1
    while i>= 0 and carry:
        if digits[i] < 9:
            digits[i] += 1
            carry = False
        else:
            digits[i] = 0
        i -=1
    if carry:
            digits.insert(0,1)
    return digits
    


print(plusOne([1,2,3,5]))
