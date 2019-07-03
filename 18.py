z,y=map(int,input().split())
for j in range(z+1,y):
  ch=j
  fnd=0
  while (j>0):
    z=j%10
    fnd=fnd+(z**3)
    j=j//10
    if(fnd==ch):
      print(fnd,end=" ")
