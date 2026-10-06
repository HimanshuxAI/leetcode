def threesum(arr):
    if len(arr)<=0:
        return arr
    arr.sort()
    res=[]
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=len(arr)-1
        while j<k:
            total=arr[i]+arr[j]+arr[k]
            if total > 0:
                    k -= 1
            elif total < 0:
                    j += 1
            else:
                    res.append([arr[i], arr[j], arr[k]])
                    j += 1

                    while arr[j] == arr[j-1] and j < k:
                        j += 1
        
        return res
        