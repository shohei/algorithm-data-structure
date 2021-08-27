#!/usr/bin/env python

def quicksort(a, left, right):
    if((right-left) <=1):
        return
    pivot_index = (left+right)//2
    pivot = a[pivot_index]
    a[pivot_index],a[right-1] = (a[right-1],a[pivot_index])
    
    i = left
    for j in range(left,right-1):
        if(a[j]<pivot):
            a[i],a[j]=(a[j], a[i])
            i+=1

    a[i],a[right-1] = (a[right-1],a[i])
    quicksort(a,left,i)
    quicksort(a,i+1,right)
    return a

xs = [10,12,15,3,8,17,4,1]
N = len(xs)
print("before:",xs)
xs=quicksort(xs,0,N)
print("after:",xs)







