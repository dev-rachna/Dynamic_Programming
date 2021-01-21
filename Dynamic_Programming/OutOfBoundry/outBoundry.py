'''
688. Knight Probability in Chessboard

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
'''
def fun( N, K, r, c):
    dp=[[0 for i in range(N)] for _ in range(N)]
    dp[r][c]=1

    for k in range(K):
        dp2=[[0 for i in range(N)] for _ in range(N)]
        for r,row in enumerate(dp):
            for c,val in enumerate(row):
                for r1,c1 in [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,2)]:
                    if 0<=r1+r<N and 0<=c1+c<N:
                        dp2[r1+r][c1+c]+=val/8.0
        
        dp=dp2
    return sum(map(sum,dp))

