an=int(input())
temp=an
val=0
while(an>0):
  p=an%10
  val=val*10+p
  an=an//10
if(temp==val):
  print("yes")
else:
  print("no")
