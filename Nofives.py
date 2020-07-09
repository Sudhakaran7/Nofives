n,m=map(int,input().split())
flag=0
count=0
arr=[]
for i in range(n,m+1):
  while(i>0):
    digit=i%10
    arr.append(digit)
    i=i//10
  for k in range(0,len(arr)):
    if(arr[k]==5):
      break
    else:
      flag+=1
  if(flag==2):
    count+=1
  arr=[]
  flag=0
print(count)
