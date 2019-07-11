an=list(input())
pr=[]
for i in an:
    if i not in pr:
        pr.append(i)
if(an==pr):
    print("Yes")
else:
    print("No")
