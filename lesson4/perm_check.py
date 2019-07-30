def solution(A):
    n = len(A)
    count = [0] * n
    for i in A:
        if i > n:
            return 0
        else:
            count[i - 1] = 1
    return min(count)