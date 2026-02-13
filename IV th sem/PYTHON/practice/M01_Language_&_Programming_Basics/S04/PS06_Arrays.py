'''
1. List ==> Built-in Data sturture
  1. use [] to create a list
  2. List is mutable
  3. List is heterogenous
  4. List is indexed
  5. List is ordered
  6. List allows duplicate values
2. Array using array module
3. Array using numpy module 
'''
'''
li=[1,12.5,True,1,"Python",2+5j]
print(li,type(li))

#No.of elements len()
print(len(li))

#Update
li[2]=False
print(li)

#Adding element ==> append(),insert()
li.append(100)
print(li)

li.insert(1,100)
print(li)

li.insert(20,200)
print(li)

li.insert(-20,300)
print(li)

li.extend([300,400,500])
print(li)

#pops the element from the end
li.pop()
print(li)

#Pops the mentioned element
li.pop(1)
print(li)

#This will not print as there is no index value as 20 in the above list
#li.pop(20)
#print(li)

#Remove element from the list
li.remove(100)
print(li)

#clears the whole list
li.clear()
print(li)

#copy() method
l1=[1,2,3]
l2=l1
l3=l1.copy()
print(l1,l2,l3)

l1.append(4)
print(l1,l2,l3)


from array import array
arr=array('i',[10,20,30])
print(arr,type(arr))

'''

