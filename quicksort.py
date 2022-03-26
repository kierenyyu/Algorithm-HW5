import numpy as np
import time


def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

num=input("数组大小：")
num =int(num)
data = np.random.randint(0,2**31,size=num)
n=len(data)
t0=time.time()
quicksort(data,0,n-1)
print(time.time()-t0,"s")
print(data)