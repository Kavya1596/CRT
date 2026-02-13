'''
#1. Count the number of digits in a number.

#n=1567
#n%10 ==> last digit
#n//10 ==> quotient

n=int(input())
count=0
while n>0:
    count+=1
    n=n//10
print(count)

#2. Sum of the digits in the number
n=int(input())
s=0
while n>0:
    s+=(n%10)
    n=n//10
print(s)

#using map function
n=int(input())
print(sum(list(map(int,str(n)))))

#3. Find digital root of a number
n=int(input())
while n>10:
    n=sum(list(map(int,str(n))))
print(n)
'''
#4. Find the number of odd and even digits.
n=int(input())
even=0
odd=0
while n>0:
    d=n%10
    if d%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)