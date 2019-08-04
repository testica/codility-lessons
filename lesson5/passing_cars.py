def solution(A):
    totalEastCars = 0
    totalPairs = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            totalEastCars += 1
        elif totalEastCars > 0:
            totalPairs += totalEastCars
            if totalPairs > 1000000000:
                return -1
    return totalPairs
