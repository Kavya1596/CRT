'''
li=[1,2,3,4,5]
#output:[2,4,6,8,10]
res =[]
for ele in li:
    res.append(ele*2)
print(res)
print([ele*2 for ele in li])

li=[1,2,3,4,5]
res=[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)
print([i for i in li if i%2==0])
print(tuple(i for i in li if i%2==0))
print({i:i*2 for i in li if i%2==0})

li1=['a','b','c']
#"a b c"
res=" "
for ch in li1:
    res=res+ch+" "
print(res)
print(' '.join(li1))

Intermediate patterns
1. Pyramid
n=4
Output:-
   *
  * *
 * * *
* * * *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

2. Inverted Pyramid
n=4
Output:-
* * * *
 * * *
  * *
   *
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

3. Diamond
n=4
Output:-
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
    
4. Palindrome Pattern
n=4
Output:-
1
212
32123
4321234
n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()
'''