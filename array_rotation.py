n,r=list(map(int,input().split()))
arr=list(map(int,input().split()))
result=[0]*n
r=(n-1)-r%n
for i in range(n):
    result[r-i]=arr[n-1-i]
print(*(result))
