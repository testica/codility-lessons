def int_to_bin(n):
    return bin(n)[2:]

def solution(N):
    count = 0
    gaps = [0]
    for i in int_to_bin(N):
        if i == '0':
            count += 1
        else:
            gaps.append(count)
            count = 0
    return max(gaps)