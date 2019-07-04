getin=int(input())
ant1,ant2=0,1
print(ant2,end=" ")
for i in range(1,getin):
  nil=ant1+ant2
  print(nil,end=" ")
  ant1,ant2=ant2,nil
