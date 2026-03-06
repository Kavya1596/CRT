'''LeetCode:- 
1480:-Running Sum of 1d Array
method 1:-
nums=[1,2,3,4]
res=[]
s=0
for ele in nums:
    s=s+ele 
    res.append(s)
print(res)

method 2:-
nums=[1,2,3,4]
ans=[]
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)

217:- Contains Duplicate
method 1:-
nums=list(map(int,input().split()))
s=set(nums)
if len(nums)!=len(s):
    print("true")
else:
    print("false")

method 2:-
nums=[1,2,3,1]
print(not(nums==list(set(nums))))

1672:-Richest Customer Wealth
method 1:-'''
accounts=[[1,2,3],
          [3,2,1]]
max_sum=sum(accounts[0])
for i in range(len(accounts)):
    if sum(accounts[i])>max_sum:
        max_sum=sum(accounts[i])
print(max_sum)