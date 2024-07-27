
S=input()
L=['dream','dreamer','erase','eraser']

dp=[False]*(len(S)+1)
dp[0]=True

for i in range(len(S)+1):
    if i>4:
        if (dp[i-5])&(S[i-5:i] in L):
            dp[i]=True
    if i>5:
        if (dp[i-6])&(S[i-6:i] in L):
            dp[i]=True
    if i>6:   
        if (dp[i-7])&(S[i-7:i] in L):
            dp[i]=True


if dp[len(S)]:
    print('YES')
else:  
    print('NO')