str=input()
for v in range(0,len(str)):
   if(str[v].isalpha() and str[v].isdigit()):
    print("No")
else:
  print("Yes")
