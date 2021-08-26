#!/usr/bin/env python
import numpy as np

S = "logistic"
T = "algorithm"

INF = 9999 
dp = np.ones((len(S)+1,len(T)+1))*INF
dp[0][0]=0

def chmin(a,b):
    if(a<=b):
        return a
    else:
        return b

for i in range(len(S)+1):
    for j in range(len(T)+1):
        if (i>0 and j>0):
            if S[i-1]==T[j-1]:
                dp[i][j] = chmin(dp[i][j],dp[i-1][j-1])
            else:
                dp[i][j] = chmin(dp[i][j],dp[i-1][j-1]+1)
        if (i>0):
            dp[i][j] = chmin(dp[i][j],dp[i-1][j]+1)
        if (j>0):
            dp[i][j] = chmin(dp[i][j],dp[i][j-1]+1)

print(dp)
