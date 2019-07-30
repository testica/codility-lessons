def total_expected(A):
    size = len(A) + 1
    return int((size * (1 + size)) / 2)

def solution(A):
    current_total = 0
    for i in A:
        current_total += i
    return total_expected(A) - current_total
