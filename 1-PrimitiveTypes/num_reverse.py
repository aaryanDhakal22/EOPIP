# Reverse numbers while in decimal

# Basically mod and remove and add to result and divide to remove
# the last digit

# O(n)
# O(1)


def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result
