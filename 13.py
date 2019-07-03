an=int(input())
if an>1:
  for i in range(2,an):
    if an%i==0:
      print("no")
      break
  else:
       print("yes")
else:
    print("no")
