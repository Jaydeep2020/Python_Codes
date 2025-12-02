def sortarr(arr):
    for i in range(0, len(arr)-1):
        min = arr[i]
        index = i
        for j in range(i+1,len(arr)):
            if arr[j] < min:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        
    return arr

arr = [12,5,3,100,1]
print(sortarr(arr))
