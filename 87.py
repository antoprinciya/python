pr,mm=map(int,input().split())
nn=[]
tc=[]
gcd=1
for i in range(1,pr+1):
    if(pr%i==0):
        nn.append(i)
for j in range(1,mm+1):
    if(mm%j==0):
        tc.append(j)
for y in nn:
    if y in tc:
        gcd=gcd*y
print(gcd)
