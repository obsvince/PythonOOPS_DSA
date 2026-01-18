# https://leetcode.com/problems/maximum-subarray/description/
"""
Kadane's Algorithm.

Always consider positive sum and carry it forward. If the next value makes the sum negative, make it 0.

[ -2, 7, -3, 4 ]

-> Discard -2, start from 7  ( positive).
-> 7 -3 = 4 ( as sum is positive, carry it forward ) [ maybe this 4 can be added to next value providing us with another max sum.
-> 4 + 4 = 8 ( indeed we got a max sum ).
Thanks to : https://www.youtube.com/watch?v=hLPkqd60-28
"""


def max_sum_subarray(nums):
    max_sum = -float('inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0
    return max_sum


def max_sum_subarray_index(nums):
    max_sum = -float('inf')
    current_sum = 0
    start_index = 0
    end_index = 0

    for i in range(len(nums)):

        if current_sum == 0:
            start_index = i

        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i

        if current_sum < 0:
            current_sum = 0
    return [start_index, end_index]


if __name__ == '__main__':
    print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_subarray([1]))
    print(max_sum_subarray([5, 4, -1, 7, 8]))

    print(max_sum_subarray_index([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_subarray_index([1]))
    print(max_sum_subarray_index([5, 4, -1, 7, 8]))
