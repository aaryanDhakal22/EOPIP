# Divide two numbers using bit manipulation

# You gradually subtract powers of 2 from higher to lower from the
# divident until you gesomething less than the divisor

# O(n)
# O(1)


def divide(x, y) -> int:
    quotient = 0
    power = 32
    y_power = y << power
    counter = 0
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
            counter += 1

        quotient += 1 << power
        x -= y_power
        counter += 1
        print(counter)
    return quotient
