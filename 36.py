mytxt2=input()
count=0
for i in range(len(mytxt2)):
  if(mytxt2[i].isdigit() or mytxt2[i].isalpha() or mytxt2[i]==(" ")):
    continue
  else:
    count+=1
print(count)
