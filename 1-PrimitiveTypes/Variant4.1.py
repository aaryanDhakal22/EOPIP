#Right propagate the rightmost set bit in x, e.g., turns (01010000) to (01011111).
def propogate(x):
    
    return x| (x-1)

#This works because when modding by a power of 2 the final n bits matter and since the n = the power of 2 -1 we 
# we can use that as a mask and filter out the necessary bits needed with an AND gate
def mod_2(x,d):

    return x&(d-1) 

def check_power_of_2(x):
    return (x&(x-1)) == 0
