n=int(input())
xy=[]
for _ in range(n):
	x,y=map(int,input().split())
	xy.append([x,y])
    
ans=0
for i in range(n):
	for j in range(n):
		ans+=((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5
print(ans/n)