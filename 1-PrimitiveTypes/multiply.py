# Multiply two numbers using bit

# If there is set bit in x then add 2ky to the result also in add
# the carry basically finds out where the set bits in both are common
# and later is shifter to represent carry overs

# O(log(x)log(y))
# O(1)


def multiply(x, y):
    result = 0

    def add(a, b):
        while b != 0:

            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    while x:
        if x & 1:
            result = add(result, y)
        x, y = x >> 1, y << 1
    return result
