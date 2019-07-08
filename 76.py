name=int(input())
for i in range(2,name):
    if name%i==0:
        print("yes")
        break
else:
    print("no")
