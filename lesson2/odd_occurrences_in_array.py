
def solution(A):
    dic = {}
    for i in A:
        if dic.get(i, False) == True:
            dic.pop(i)
        else:
            dic[i] = True
    return list(dic)[0]
