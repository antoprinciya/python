num=int(input())
nums=list(map(int,input().split()))
for v in range(len(nums)-1):
   if(nums[v]>nums[v+1]):
      print(v)
