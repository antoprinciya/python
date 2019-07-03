p,r=map(int,input().split())
for i in range(p+1,r,1):
    if(i>1):
        for v in range(2,i):
            if(i%v==0):
                break
        else:
            print(i,end=" ")
