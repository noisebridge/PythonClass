#! /usr/bin/env python
import numpy
values = numpy.random.randint(low=-100, high=100, size=100)


def solution_1(values):
    current_max = 0
    for i in range(len(values)):
        for j in range(i, len(values)):
            current_max = max(current_max, sum(values[i:j]))

    return current_max


def solution_2(values):
    current_max = 0
    for i in range(len(values)):
        current_sum = 0
        for val in values[i:]:
            current_sum += val
            current_max = max(current_max, current_sum)

    return current_max


def solution_3(values):
    cumulative = numpy.zeros(len(values) + 1, dtype=int)
    current_sum = 0

    # This is equivalent to itertools.accumulate plus a leading zero
    for i, v in enumerate(values):
        current_sum += v
        cumulative[i + 1] = current_sum

    current_max = 0
    for i, cumulative_i in enumerate(cumulative):
        for j, cumulative_j in enumerate(cumulative[i:]):
            current_sum = cumulative_j - cumulative_i
            current_max = max(current_max, current_sum)

    return current_max


def solution_4(values):
    current_max = 0
    max_ending_here = 0

    for val in values:
        max_ending_here = max(max_ending_here + val, 0)
        current_max = max(current_max, max_ending_here)

    return current_max


if __name__ == '__main__':
    print(solution_1(values))
