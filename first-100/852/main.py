from typing import List


# complexity: time - O(log n) | space - O(1), where n length of arr
def peakIndexInMountainArray(arr: List[int]) -> int:
    low = -1
    high = len(arr)

    while low + 1 < high:
        middle = (low + high) // 2
        if arr[middle] > arr[middle + 1]:
            high = middle
        else:
            low = middle

    return high


print(peakIndexInMountainArray([0, 10, 5, 2]))  # 1
