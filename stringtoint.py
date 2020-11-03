def myAtoi(s: str) -> int:
        negative= False
        found= False
        result = 0
        dict= {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in s:
            if (i == "-" or i == "+") and not found:
                found=True
                negative = True if i== "-" else False
            elif i in dict:
                found=True
                result=result*10+dict[i]
            elif i != " " or (i==" " and found) :
                break
        if negative:
            return -result if result<2**31 else -(2**31)
        return result if result<2**31-1 else 2**31-1
                
print(myAtoi("      -11919730356x"))