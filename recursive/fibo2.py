#!/usr/bin/env python
# use loop not recursion

def fibo(N):
    F0 = 0
    F1 = 1
    for i in range(2,N+1):
        F2 = F0 + F1 
        F0 = F1
        F1 = F2
    return F2 

N = int(input("N := "))
F = fibo(N)


print("Fibonacci number (N={}) is {}".format(N,F))

