N,M=map(int,input().split())
L_f=[[] for i in range(N)]
for i in range(M):
    u,v=map(int,input().split())
    L_f[u-1].append(v-1)
S,T=map(int,input().split())
from collections import deque
queue=deque()
queue.append([S-1,0])
dist_list=[[-1,-1,-1] for i in range(N)]
dist_list[S-1][0]=0

while queue:
    v=queue.popleft()
    v_p=v[0]
    v_d=v[1]

    for j in L_f[v_p]:
        dist=[j,v_d+1]
        if j==T-1 and (v_d+1)%3==0:
            print((v_d+1)//3)
            exit()
        if dist_list[j][(v_d+1)%3]==-1:
            dist_list[j][(v_d+1)%3]=v_d+1
            queue.append(dist)

print(-1)


