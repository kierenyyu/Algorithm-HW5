import numpy as np
import time

def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

num=input("数组大小：")
num =int(num)
data = np.random.randint(0,2**31,size=num)
n=len(data)
t0=time.time()
insertionsort(data)
print(time.time()-t0,"s")
print(data)