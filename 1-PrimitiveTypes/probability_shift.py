# Turn a probability higher

# The you shift the probability is by making multiple calls
# to the generator and finally once u are able to represent
# the number of outcomes with the nearest numbers of
# sample space then the next thing to do is to
# have a result that is within the number of outcomes
# for eg [1,2,3,4] but n = 3 so u have make sure ure
# results are less than 3.
# since the numbers can be denoted with log2(n) bits
# we make log2(b-a+1) calls

# O(log2(b-a+1))
# O(1)


def prob_shift(a, b, func):
    number_of_outcomes = b - a + 1

    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | func()
            i += 1
        if result < number_of_outcomes:
            break
    return result + a
