def multiply(x, y):
    result = 0

    def add(a, b):
        while b != 0:
            # the carry basically finds out where the set bits in both are common
            # and later is shifter to represent carry overs
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    while x:
        if x & 1:  # if last digit is one
            result = add(result, y)
        x, y = x >> 1, y << 1
    return result


print(add(5, 6))
