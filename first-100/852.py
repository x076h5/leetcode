from typing import List


# complexity: time - O(log n) | space - O(1), where n length of arr
def peakIndexInMountainArray(arr: List[int]) -> int:
    low = 0
    high = len(arr) - 1

    while low < high:
        middle = (low + high) // 2
        target = arr[middle + 1]
        if target > arr[middle]:
            low = middle + 1
        elif target < arr[middle]:
            high = middle

    return low


print(peakIndexInMountainArray([0, 10, 5, 2]))  # 1
