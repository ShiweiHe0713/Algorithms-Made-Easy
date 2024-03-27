def isPalindrome(S,p,q) -> bool:
    n = q - p + 1
    if n <= 1: return True
    l = p + n // 2 - 1
    r = q - n // 2 + 1
    while l >= p and r <= q:
        if S[l] != S[r]:
            return False
        l -= 1
        r += 1
    return True


def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]
 
    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):
 
                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
 
    return m[1][n-1]




str = "ABACIOHO"
if isPalindrome(str,4,7):
    print("True")
else:
    print("False")
