def able_to_jump(path):
    for i in path:
        if i == -1:
            return False
    return True


def solution(X, A):
    path = [-1] * X
    for time in range(0, len(A)):
        pos = A[time] - 1
        if path[pos] == -1:
            path[pos] = time
        elif path[pos] > time:
            path[pos] = time

    if able_to_jump(path):
        return max(path)
    return -1
