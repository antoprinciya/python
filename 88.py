ge10,se10=map(int,input().split())
maxima=max(ge10,se10)
while(1):
 if(maxima%ge10==0 and maxima%se10==0):
  print(maxima)
  break
 maxima+=1
