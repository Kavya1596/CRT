'''
Optimization: process of modifying the code to reduce the time compexity
Brute Force --. trying of all possible combinations
optimal solution --. needs thinking,low complexity
Optimization Basics : Making the sution 

a=[10,20,30,40,52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i]+a[j])  #O(n^2)

a=[10,20,30,40,52]
for num in a:
    print(num+num)      #O(n)

why optimization is important?
--> improves programs speed
--> reduces memory usage
--> avoid nested loops
'''
a=[10,20,30,40,52]
for num in a:
    print(num+num)

a=[10,20,30,40,52]
sum1=0
for i in range(len(a)):
    sum1+=a[i]
print(sum)

a=[10,20,30,40,52]
print(sum(a))

a=[]
for i in range(10):
    a.append(i*i)
print(a)

a=print([i*i for i in range(10)])

#2) find the maximum ele in a list

