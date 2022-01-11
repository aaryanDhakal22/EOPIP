# BRUTE FORCE
# isolate the ith and the jth bit and store in variable
# clear the ith and jth
# use OR with the local varibale to combile 

# Optimised : O(1)
def swap_bits(x,i,j):
    if (x>>i) & 1 != (x>>j) & 1:
        #ith and jth both differ. We will swap by flipping each value.
        bit_mask = (1<<i) | (1 << j) # since 1's can be used with XOR to swap
        x^= bit_mask
    return x
