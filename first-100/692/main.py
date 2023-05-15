import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        s_freq = Counter(words)

        heap = []

        for s, freq in s_freq.items():
            heap.append((-freq, s))

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    instance = Solution()
    # print(instance.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))  # ["i", "love"]
    print(instance.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    # ["the","is","sunny","day"]
