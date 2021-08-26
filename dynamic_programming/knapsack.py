#!/usr/bin/env python
import numpy as np
np.set_printoptions(linewidth=100)

wvs = [(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)]
n = len(wvs)
W = sum([wv[0] for wv in wvs])

dp = np.zeros((n+1,W+1))

def chmax(a,b):
    if a>=b:
        return a
    else:
        return b

for i in range(1,n+1):
    for w in range(W+1):
        if(w-wvs[i-1][0]>=0):
            dp[i][w] = chmax(dp[i-1][w],dp[i-1][w-wvs[i-1][0]]+wvs[i-1][1])
        dp[i][w]  = chmax(dp[i][w],dp[i-1][w])

print(dp)


