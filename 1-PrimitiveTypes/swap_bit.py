# Swap the Bits

# If they different then only swap else useless. To swap
# get 2 1's in the ith and jth position using shifting and OR'ing
# then XOR to flip

# O(1)
# O(1)


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x
