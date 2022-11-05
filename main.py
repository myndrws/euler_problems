# author: amy
# project euler problems

def p1_sum_of_multiples(multiple1, multiple2, max_n):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    :param multiple1: multiple for condition 1
    :param multiple2: multiple for condition 2
    :param max_n: the max number under which to sum the multiples of multiple1 or multiple2
    :return: generator
    """
    for i in range(max_n):
        if i % multiple1 == 0 or i % multiple2 == 0:
            yield i


if __name__ == "__main__":

    print(f"Answer to problem 1: {sum(p1_sum_of_multiples(3, 5, 1000))}")
