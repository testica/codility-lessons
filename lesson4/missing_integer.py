def remove_positive_integers(A):
    keep_positives = []
    for i in A:
        if i > 0:
            keep_positives.append(i)
    return keep_positives


def get_minor_missing_int(A):
    for i in range(0, len(A)):
        if A[i] == False:
            return i + 1


def solution(A):
    A = remove_positive_integers(A)
    sec = [False] * 1000000
    for i in A:
        sec[i - 1] = True

    return get_minor_missing_int(sec)
