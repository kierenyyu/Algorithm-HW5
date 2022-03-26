import numpy as np
import time

def radixSort(arr):
    n = len(str(max(arr)))
    for k in range(n):

        bucket_list=[[] for i in range(10)]
        for i in arr:

            bucket_list[i//(10**k)%10].append(i)

        arr=[j for i in bucket_list for j in i]
    return arr

num=input("数组大小：")
num =int(num)
data = np.random.randint(0,2**31,size=num)
n=len(data)
t0=time.time()
data = radixSort(data)
print(time.time()-t0,"s")


