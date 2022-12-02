# author: amy
# project euler problems

from itertools import filterfalse


def sum_multiples(multiple1, multiple2, max_n):
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


def p1_sum_multiples(*args):
    """
    Runs p1 to get the answer printed.
    :param args:
    :return:
    """
    answer = sum(sum_multiples(*args))
    print(f"Answer to problem 1: {answer}")
    return None


def fib_seq(max_n):
    """
    Gets the fib sequence wihtout storing in memory/
    :param max_n: the maximum number to get to in the fib sequence
    :return:
    """
    n1 = 0
    n2 = 1
    while n2 <= max_n:
        next_n = n1 + n2
        if next_n <= max_n:
            yield next_n
        n1 = n2
        n2 = next_n


def p2_fib_sum_even(max_n):
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
    :return:
    """
    answer = sum(filterfalse(lambda x: x % 2, fib_seq(max_n)))
    print(f"Answer to problem 2: {answer}")
    return None


if __name__ == "__main__":
    p1_sum_multiples(3, 5, 1000)
    p2_fib_sum_even(4000000)
