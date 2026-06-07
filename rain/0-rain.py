#!/usr/bin/python3
"""
Module for calculating rainwater retention
"""


def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    total = 0

    for i in range(n):
        max_left = max(walls[0:i+1])
        max_right = max(walls[i:])
        water = min(max_left, max_right) - walls[i]
        total += water

    return total
