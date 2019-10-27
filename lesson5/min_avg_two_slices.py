def solution(A):
    size = len(A)
    sum_prefix = [0] * size

    sum_prefix[0] = A[0]

    for i in range(1, size):
        sum_prefix[i] = sum_prefix[i - 1] + A[i]

    print(sum_prefix)
    min_avg = 10000
    start_pos = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            if i == 0:
                avg = sum_prefix[j] / (j - i + 1)
            else:
                avg = (sum_prefix[j] - sum_prefix[i - 1]) / (j - i + 1)

                print(i, j, avg)

            if avg < min_avg:
                start_pos = i
                min_avg = avg
    return start_pos


print(solution([10000, -10000]))
