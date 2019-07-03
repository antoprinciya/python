df,as=map(int,input().split())
for p in range(df+1,as,1):
    if(p>1):
        for f in range(2,p):
            if(e%f==0):
                break
        else:
            print(p,end=" ")
