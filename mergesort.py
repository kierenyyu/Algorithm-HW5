import numpy as np
import time

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

num=input("数组大小：")
num =int(num)
data = np.random.randint(0,2**31,size=num)

n=len(data)
t0=time.time()
mergeSort(data,0,n-1)
print(time.time()-t0,"s")
print(data)