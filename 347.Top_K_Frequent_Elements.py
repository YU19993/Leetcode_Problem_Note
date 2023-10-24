def topKFrequent(nums: list[int], k: int) -> list[int]:
    from collections import defaultdict

    # Build a frequency map
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # Use buckets to store numbers by their frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # Extract the k most frequent elements
    res = []
    for bucket in reversed(buckets):
        for num in bucket:
            if k > 0:
                res.append(num)
                k -= 1

    return res

# Test cases for validation
assert set(topKFrequent([1,1,1,2,2,3], 2)) == {1,2}
assert set(topKFrequent([1], 1)) == {1}
