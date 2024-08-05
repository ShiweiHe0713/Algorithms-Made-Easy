def calc(T, L, n, k, i, j):
    # T[i,j]: i stands for the first i boards, j means the number of painters
    for j in range(0,k): 
        T[0][j] = 0
    for i in range(1, n):
        T[i][1] = L[i]

def min_time(n, k):
    # n * k
    T = [[0]*k]*n
    for i in range(0, n):
        T[i][1]
    


'''
We want to paint our new fence, which is made up $N$ boards. The
lengths of the $N$ boards are given in array
$L = (L[1], L[2], \ldots, L[N])$. We have hired $K$ painters, where
each painter takes $1$ hour to paint $1$ unit of board. For example,
if one of the painters paints boards $3$, $4$ and $5$, then she
completes at time $t_i=L[3]+L[4]+L[5]$. Our goal is to assign each
painter to some subset of boards, to minimize the time when the fence
has been completely painted. Since the $K$ painters can work in
parallel, this corresponds to minimizing $\max(t_1,\ldots,t_K)$, where
$t_i$ is the time taken by painter $i$ to complete her job. The
painting task must be accomplished under the following constraints:

- Each board must be completely painted by exactly one painter;
i.e., no board can be painted partially by one painter and partially
by another.
- Each painter paints a contiguous collection of boards.  For example, a
configuration where painter $1$ paints boards $1$ and $3$ but not
$2$ is not a valid solution.

You are given as input the following: the number of painters $K$, and
an array $L$ with the board lengths.  In the following problems,
denote by $T[i,j]$ the minimum time to paint the first $i$ boards using
$j$ painters. We will, successively in the following subtasks, come up
with a procedure to minimize the painting time.
'''