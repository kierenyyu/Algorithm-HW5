import numpy as np
import time


def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)

num=input("数组大小：")
num =int(num)
data = np.random.randint(0,2**31,size=num)

n=len(data)
t0=time.time()
shellSort(data)
print(time.time()-t0,"s")
print(data)