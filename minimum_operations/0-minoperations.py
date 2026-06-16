#!/usr/bin/python3
"""Minimum number of operations to reach n H characters"""


def minOperations(n):
    """Calculate the fewest number of operations to reach exactly n H characters"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations