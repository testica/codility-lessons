def solution(A):
    total_sum = sum(A)
    current_sum = 0
    diffs = []
    for p in range(1, len(A)):
        current_sum += A[p - 1] 
        diffs.append(abs(current_sum - (total_sum - current_sum)))
    return min(diffs)