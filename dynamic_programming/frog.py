#!/usr/bin/env python

h=[2,9,4,5,1,6,10]
N = len(h)
dp = [0]*N

def find_cost(h):
    for i in range(1,len(h)):
        cost1 = abs(h[i]-h[i-1])
        cost2 = 99999
        if i-2>=0:
            cost2 = abs(h[i]-h[i-2])
        if cost1<=cost2:
            dp[i] = dp[i-1]+cost1
        else:
            dp[i] = dp[i-2]+cost2
    print(dp)
    return dp[-1]

cost = find_cost(h)

print("minimum cost:",cost)


