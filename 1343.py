# complexity: time - O(n), where n - length of arr | space - O(1)
def numOfSubarrays(arr, k, threshold):
    win_start = 0
    win_sum = 0
    counter = 0

    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        win_size = win_end - win_start + 1
        if win_size >= k:
            cur_average = win_sum / k
            if cur_average >= threshold: counter += 1
            win_sum -= arr[win_start]
            win_start += 1

    return counter


print(numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))  # 3
print(numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))  # 6
