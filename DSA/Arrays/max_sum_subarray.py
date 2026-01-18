def maxSubarraySum(arr):
    # Stores the result (maximum sum found so far)
    res = arr[0]

    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        # Either extend the previous subarray or start
        # new from current element
        current_number = arr[i]
        print("At start: maxEnding:", maxEnding, ", res:", res)
        prev_sum = maxEnding + arr[i]
        print("current element: ", current_number, ", maxEnding + arr[i]: ",
              prev_sum, f" i.e., {maxEnding} + {arr[i]}")
        maxEnding = max(prev_sum, current_number)

        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)

        print("At end: maxEnding:", maxEnding, ", res:", res)


    return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    # arr = [-1, -2, -3, -12, -3]
    print(arr)
    print(maxSubarraySum(arr))
