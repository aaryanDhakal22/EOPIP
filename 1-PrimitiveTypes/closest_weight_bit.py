# Change bits such that their difference is minimum

# The key factor is to alter the LSB to make sure the difference is as small as possible
# for the find two that can be flipped and flip them while LSB is as less as possible

# O(n)
# O(1)


def closest_int_same_bit_count(x):
    BIT_SIZE = 8
    for i in range(BIT_SIZE - 1):
        if ((x >> i) & 1) != (x >> (i + 1) & 1):
            x ^= (1 << i) | (1 << (i + 1))
            return x
    raise ValueError("All bits are either 0 or 1")
