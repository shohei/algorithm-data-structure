#!/usr/bin/env python
#use recursion and memo (dynamic programming)

N = int(input("N := "))
memo = [None]*(N+1)

def fibo(N):
    global memo
    if (N==0):
        return 0
    if (N==1):
        return 1
    if (memo[N]!=None):
        return memo[N]
    memo[N]=fibo(N-1)+fibo(N-2)
    return memo[N]

F = fibo(N)
print("Fibonacci number (N={}) is {}".format(N,F))

