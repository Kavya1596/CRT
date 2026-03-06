'''Set:-
1. use {} to create a set
2. set does not allow duplicates
3. set unindexed
4. set is unordered
5. set is heterogenous
6. set is mutable

s={True,10,12.45,10,1,9+5j}
print(s,type(s))

Tuples:-
1) Definition:- it is ordered and immutable collection of data.
2) Immutable
3) Accessing--> index positions +ve or -ve
4) Concatenation--> +
5) Nesting of tuples--> tuple inside a tuple
6) Repetition of tuples
7) Slicing of tuples
8) Deleting a tuple
9) Leetcode problems on tuples(349,657) 

t=(10,23)
t[0]=50  #we cannot change bcz tuples are immutable 
print(t)

t=(10,23,50,12,45,32,48)
t2=("sai","kalyani","krishna")
print(t[0])
print(t[-1])
print(t+t2)
print(t,t2)
print(t*5)
print(t[1:4])
print(t[:5])
print(t[:-1])
del t 

349:- Intersection of two arrays
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
set1=set(nums1)
set2=set(nums2)
print(list(set1.intersection(set2)))

657:-Robot Return to Origin
moves=input()
if  moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L'):
    print("TRUE")
else:
    print("FALSE")

Dictionary:-
d={"a":'Sai'}
print(d)
d2=dict(a='Sai',b='Kalyani',c='Krishna')
print(d2)
print(d2['a'])
print(d2.get('b'))
print(d2.keys())
print(d2.values())
print(d2={'age':25})
'''
'''deleting of dictionary
1) del -->
2) pop() --> removes key returns value
3) popitem() --> removes last inserted key value pair returns it as tuple 
4) clear() --> removes entire dictionary
'''
