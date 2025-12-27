def merge_arrays(arr1, arr2):
    sorted_arr = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


if __name__ == '__main__':
    print(merge_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
    print(merge_arrays([1, 7, 8, 11, 12], [6, 7, 8, 9, 10]))
