def convert(s, numRows):
    if len(s) == 1:
        return numRows
    if len(s) == 0:
        return ""
    result = ""
    counter = 2*numRows-2
    for i in range(numRows):
        j =0
        print('i changed to', i)
        while (i+j)<len(s):
            print("J changed to", j,s[i+j])
            result += s[i+j]
            if i!= 0 and i!= numRows-1 and j+counter-i<len(s):
                result += s[j+counter-i]
            j+= counter
    return result

convert('AB', 1)
            

        
        
        


