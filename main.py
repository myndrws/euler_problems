# author: amy
# project euler problems

from itertools import filterfalse


def sum_multiples(multiple1: int, multiple2: int, max_n: int):
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


def fib_seq(max_n: int):
    """
    Gets the fib sequence without storing in memory/
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


def p2_fib_sum_even(max_n: int) -> None:
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
    :return:
    """
    answer = sum(filterfalse(lambda x: x % 2, fib_seq(max_n)))
    print(f"Answer to problem 2: {answer}")
    return None


def largest_prime(input_n: int, recur: bool = False) -> int | None:
    """
    Determine what the largest prime factor of the input number is.
    First determine the number is a factor, then determine if that is prime.
    Using recursion.
    :return: int, the largest prime factor
    """

    for i in reversed(range(2, input_n)):
        if (input_n % i) == 0 and not recur:   # just tests if it's a factor
            # now test if it's a prime factor by forwarding through recursion
            if largest_prime(input_n=i, recur=True) is not None:
                return i
        elif (input_n % i) == 0 and recur:
            return None

    if recur:
        return input_n


def p3_largest_prime_factor(input_n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    :return:
    """
    answer = largest_prime(input_n, recur=False)
    print(f"Answer to problem 3: {answer}")
    return None


if __name__ == "__main__":
    p1_sum_multiples(3, 5, 1000)
    p2_fib_sum_even(4000000)
    p3_largest_prime_factor(1321432)
