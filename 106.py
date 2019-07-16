A,B=map(int,input().split())
P=list(map(int,input().split()))
count=0
for v in P:
    if ((v%2)!=0):
       count=count+1
    if(count==B):
       print(v)
       break
