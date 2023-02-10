arr =  [4,1,2,1,2]


for i in range(len(arr)):
    count =0
    for j in range(len(arr)):
        if arr[i] == arr[j] and i!=j:
            count+=1
            break                   
    if count==0:
       print(arr[i])
    
