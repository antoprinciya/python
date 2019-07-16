A,P=map(int,input().split())
N=list(map(int,input().split()))
count=0
for i in N:
    if (N[i]<N[i+1]):
       count=count+1
    if(count==P):
       print(i)
       break
