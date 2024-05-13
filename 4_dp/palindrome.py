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


str = "ABACIOHO"
if isPalindrome(str,4,7):
    print("True")
else:
    print("False")
