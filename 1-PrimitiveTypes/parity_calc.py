# This approach is O(n) because it also loops for reset bits 
def parity(x):
	result = 0
	while x:
		result ^= x & 1
		x>>=1
	return result

#This approach is O(k) where k is number of set bits
def parity(x):
	result = 0
	while x:
		result ^=1
		x &= (x - 1)
	return result

# This approach is used for huge integers and uses cache to store parity of smaller integers
def parity(x):
    PRECOMPUTED_PARITY = []
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^ 
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^ 
            PRECOMPUTED_PARITY [(x >> MASK_SIZE) & BIT_MASK ] ^ 
            PRECOMPUTED_PARITY [ x & BIT_MASK])

# This approach is O(log n) and uses XOR and shifting to get the answer but keep the answer in the integer itself
def parity1(x):
    shiftamount = 1
    print("x",bin(x))
    while x >> shiftamount:
        print(shiftamount)
        x = x ^ x >> shiftamount
        print("x",bin(x))
        shiftamount <<= 1
    return x & 1

print(parity1(182))