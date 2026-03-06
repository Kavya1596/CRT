'''
Programs:
1. Find the GCD (using math module and using Eucliden method)
2. Find LCM 
3. Write a Python code to check a num is Perfect number or not

Leetcode-->412

#write python code to print all the arithmetic operators(+,-,*,/,//,**,%)?
#Important Built-in Math functions:'
print(abs(-54))
print(round(5.478))
print(min([10,20,30,40,54.2]))
print(max([10,20,30,40,54,2]))
print(sum([10,20,30,40,54,2]))
print(pow(2,5))

import math 
print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.2))
print(math.pi)
print(math.factorial(6))
'''
#1. Find the GCD (using math module and using Eucliden method)
a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b 
print(a)

import math 
a=int(input())
b=int(input())
print(math.gcd(a,b))