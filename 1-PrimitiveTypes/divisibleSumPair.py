# Find the sum pair who is divisible by a certain integer in an arry

# You modulo from the start and compute the complement and
# store the modulo that way when u see a complement that matches
# the modulo hashmap you add to the counter

# O(n)
# O(k)


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
