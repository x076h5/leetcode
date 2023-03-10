# complexity: time - O(n) | space - O(1), where n - length of arr
def numOfSubarrays(arr, k, threshold):
    win_start = 0
    win_sum = 0
    counter = 0

    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        win_size = win_end - win_start + 1
        if win_size >= k:
            average = win_sum / k
            if average >= threshold: counter += 1
            win_sum -= arr[win_start]
            win_start += 1

    return counter


print(numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))  # 3
print(numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))  # 6
