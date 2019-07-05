Names=int(input())
anto=0
i=0
while(Names>0):
    i=Names%10
    anto=anto+i
    Names=Names//10
print(anto)
