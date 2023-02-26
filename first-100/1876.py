# complexity: time - O(n), where n - length of s | space - O(1)
def countGoodSubstrings(s):
    k = 3
    win_start = 0
    counter = 0

    for win_end in range(len(s)):
        win_size = win_end - win_start + 1
        if win_size >= k:
            substr = s[win_start:win_end + 1]
            if is_good_str(substr): counter += 1
            win_start += 1

    return counter


def is_good_str(s):
    return len(set(s)) == len(s)


print(countGoodSubstrings("aababcabc"))  # 4
