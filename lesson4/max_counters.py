def solution(N, A):
    max_counter = 0
    set_max = 0
    C = [0] * N
    for i in A:
        if i >= 1 and i <= N:
            if C[i - 1] < set_max:
                C[i - 1] = set_max
            C[i - 1] += 1
            if C[i - 1] > max_counter:
                max_counter = C[i - 1]
        if i == N + 1:
            set_max = max_counter

    for i in range(0, len(C)):
        if C[i] < set_max:
            C[i] = set_max
    return C
