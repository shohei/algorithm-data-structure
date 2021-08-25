#!/usr/bin/env python
a=int(input("a:= "))
b=int(input("b:= "))

gcd = None

def find_gcd(_a,_b):
    global gcd
    r = _a % _b
    if(r==0):
        gcd = _b
        return
    find_gcd(_b, r)

find_gcd(a,b) 

print("GCD of a and b is",gcd)


