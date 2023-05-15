import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s):
        ch_freq = Counter(s)
        # print(ch_freq)
        heap = []
        for ch, freq in ch_freq.items():
            heapq.heappush(heap, [-freq, ch])

        res = ""
        for _ in range(len(heap)):
            # print(heapq.heappop(heap))
            freq, ch = heapq.heappop(heap)
            res += abs(freq) * ch

        return res


if __name__ == "__main__":
    instance = Solution()
    print(instance.frequencySort("tree"))  # eert
    print(instance.frequencySort("raaeaedere"))  # "eeeeaaarrd"
