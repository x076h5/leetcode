import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        num_freq = Counter(nums)
        heap = []

        for num, freq in num_freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))

        return [num for freq, num in heap]


if __name__ == "__main__":
    instance = Solution()
    print(instance.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
