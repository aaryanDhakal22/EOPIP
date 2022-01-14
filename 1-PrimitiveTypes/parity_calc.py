# Calculate the parity

# This approachuses XOR and shifting to get the answer but keep the answer in the integer itself

# O(log n)
# O(1)


def parity1(x):
    shiftamount = 1
    print("x", bin(x))
    while x >> shiftamount:
        print(shiftamount)
        x = x ^ x >> shiftamount
        print("x", bin(x))
        shiftamount <<= 1
    return x & 1
