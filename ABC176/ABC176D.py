H,W=map(int,input().split())
Ch,Cw=map(int,input().split())
Dh,Dw=map(int,input().split())
S=[list(input()) for _ in range(H)]

from collections import deque

def BFS(H, W, h, w):
    que = deque()
    
    dist = [[10**9] * W for _ in range(H)]
    que.append((h, w))
    dist[h][w] = 0
    while que:
        v = que.popleft()
        G = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 通常の4方向への移動
        J=[(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),(-1,-2),(-1,-1),(-1,1),(-1,2),(0,-2),(0,2),(1,-2),(1,-1),(1,1),(1,2),(2,-2),(2,-1),(2,0),(2,1),(2,2)]


        for v2 in G:
            nh, nw = v[0] + v2[0], v[1] + v2[1]
            if 0 <= nh < H and 0 <= nw < W and dist[nh][nw] > dist[v[0]][v[1]]:
                if S[nh][nw] == "#":
                    continue
                dist[nh][nw] = dist[v[0]][v[1]]
                que.appendleft((nh, nw))
        for v2 in J:    
            nh, nw = v[0] + v2[0], v[1] + v2[1]
            if 0 <= nh < H and 0 <= nw < W and dist[nh][nw] > dist[v[0]][v[1]] + 1:
                if S[nh][nw] == "#":
                    continue
                dist[nh][nw] = dist[v[0]][v[1]] + 1
                que.append((nh, nw))


    return dist

print(BFS(H, W, Ch-1, Cw-1)[Dh-1][Dw-1] if BFS(H, W, Ch-1, Cw-1)[Dh-1][Dw-1] != 10**9 else -1)