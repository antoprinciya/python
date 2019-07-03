nm=int(input())
a=list(map(int,input().split()[:nm]))
a.sort()
for v in a:
  print(v,end=" ")
