#!/usr/bin/env python

def partial_sum(a,W):
    if a==[]:
        if W==0:
            return True
        else:
            return False
    last = a[-1]
    a2 = a[:-1]
    if partial_sum(a2,W):
        return True
    elif partial_sum(a2,W-last):
        return True
    else:
        return False

#a = [3,2,6,5]
#W=14
#a = [1,3,7,10,13]
#W=21
a = [2,4,6,8,10]
W=19
result = partial_sum(a,W) 

print("Check if the partial sum {} can be made from {}... {}".format(W,a,result))



