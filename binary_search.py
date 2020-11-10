def search(arr, target, low=0, high=''):
     if not high:
         high = len(arr)-1
     if low <= high:
         mid = (low+high)//2
         if arr[mid] == target:
             return True
         elif arr[mid] < target:
             low = mid+1
             return search(arr,target,low,high)
         else:
             high = mid -1
             return search(arr,target,low,high)
     return False
    
arr= [1,2,3,5,6]
print(search(arr,1))
