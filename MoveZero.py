
arr=[1,1,4,0,4,0,3]
a=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        temp=arr[i]
        arr[i]=arr[a]
        arr[a]=temp
        a+=1
print(arr)


