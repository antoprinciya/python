a11,b12,c13=map(int,input().split())
ant=0
for v in range(0,c13):
   ant=ant+a11
   a11=a11+b12
print(ant)
