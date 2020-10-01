def quickSort(arr):
    less =[]
    bigger=[]
    equal = []
    if len(arr)==1 or len(arr)==0:
        return arr
    pivot = arr[0]
    for i in range(len(arr)):
            if arr[i] < pivot:
                less.append(arr[i])
            elif arr[i] > pivot:
                bigger.append(arr[i])
            else:
                equal.append(arr[i])
    return quickSort(bigger)+ equal + quickSort(less)
