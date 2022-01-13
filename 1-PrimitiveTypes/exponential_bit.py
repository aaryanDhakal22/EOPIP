def powerOptimised(a, n):
    # This was a moron . firstly u have to multiply regardless buit this time multiply with a
    # higher power so that u dont have to multiply more than once to get that higher power and
    # then if u get an odd one just multiply the odd to the ans and keep going with the
    # powers of 2
    ans = 1
    if n < 0:
        n, a = -n, 1.0 / a
    while n:

        if n & 1:
            ans = ans * a
        a = a * a
        n = n >> 1
    return ans


a = 2
n = -10

print(powerOptimised(a, n))
