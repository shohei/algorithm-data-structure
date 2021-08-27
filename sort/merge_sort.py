#!/usr/bin/env python

xs = [12,9,15,3,8,17,6,1]
N = len(xs)

def mergesort(a, left, right):
    if((right-left)==1):
        return
    mid = left + (right-left)//2
    mergesort(a, left, mid)
    mergesort(a, mid, right)
    buf = a[left:mid] + list(reversed(a[mid:right]))

    index_left = 0
    index_right = len(buf)-1
    for i in range(left,right):
        if(buf[index_left]<=buf[index_right]):
            a[i] = buf[index_left]
            index_left += 1
        else:
            a[i] = buf[index_right]
            index_right -= 1
    return a

print("before:",xs)
xs=mergesort(xs,0,N)
print("after:",xs)


