def shift_items_array(A):
    len_array = len(A)
    carry = A[len_array - 1]
    for i in range(0, len_array):
        aux = A[i]
        A[i] = carry
        carry = aux
    return A

def solution(A, K):
    if (len(A) == 0): return A
    for i in range(K):
        A = shift_items_array(A)
    return A