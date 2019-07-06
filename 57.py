an1,pr2=map(int,input().split())
nums=list(map(int,input().split()[:an1]))
rep=0
for i in nums:
   if(i==pr2):
      rep=rep+1
print(rep)
