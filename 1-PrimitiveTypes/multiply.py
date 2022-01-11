def multiply(x,y):
    result = 0
    def add(a,b):
        while (b!=0):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

        
    while x:
        if (x & 1): # if last digit is one
            result = add(result,y)
        x, y = x>>1 , y<<1
    return result

print(multiply(15000,3))