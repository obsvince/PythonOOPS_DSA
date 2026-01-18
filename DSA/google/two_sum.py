def getSum(arr, target):
    complement = set()

    for num in arr:
        if num in complement:
            return True

        complement.add(target - num)
    return False


# better for its naming convention and variable names used.
def has_pair_with_sum(arr, target):
    """
    Checks if any two numbers in arr add up to target.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()

    for num in arr:
        remainder = target - num
        print(num, remainder)
        if remainder in seen:
            return True
        seen.add(num)
        print(seen)

    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 9]
    arr2 = [1, 3, 4, 5]
    target = 8
    print(getSum(arr, target))
    print(getSum(arr2, target))
    # Test cases
    print(has_pair_with_sum(arr, target))  # False
    print(has_pair_with_sum(arr2, target))  # True
