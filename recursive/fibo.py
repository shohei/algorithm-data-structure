#!/usr/bin/env python

def fibo(N):
    if (N==0):
        return 0
    if (N==1):
        return 1
    return fibo(N-1)+fibo(N-2)

N = int(input("N := "))
F = fibo(N)
print("Fibonacci number (N={}) is {}".format(N,F))

