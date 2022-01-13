# def divisibleSumPairs(n, k, ar):
#     rest = [0] * k
#     nrOfPairs = 0
#     for elem in ar:
#         modu = elem % k
#         comp = k - modu
#         test3 = comp % k
#         test4 = rest[test3]
#         nrOfPairs += test4

#         rest[elem % k] += 1
#     return nrOfPairs


def divisibleSumPairs(n, k, arr):
    hMap = dict()
    counter = 0
    for item in arr:
        modu = item % k
        comp = k - modu

        if comp in hMap.keys():
            counter += hMap[comp]
        if modu in hMap.keys():
            hMap[modu] += 1
        else:
            hMap.setdefault(modu, 1)
        print(hMap)
        print("modulus", modu)
        print("comple", comp)
        print("couunter", counter, "\n")
    return counter


print(divisibleSumPairs(7, 5, [1, 2, 3, 4, 5, 6, 7]))
