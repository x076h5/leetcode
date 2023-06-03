def lengthOfLongestSubstring(s):
    memory = set()
    max_len = 0
    win_start = 0

    for win_end in range(len(s)):
        cur_ch = s[win_end]

        while cur_ch in memory:
            left_ch = s[win_start]
            memory.remove(left_ch)
            win_start += 1

        memory.add(cur_ch)
        win_size = win_end - win_start + 1
        max_len = max(max_len, win_size)

    return max_len


print(lengthOfLongestSubstring("abcabcbb"))  # 3
