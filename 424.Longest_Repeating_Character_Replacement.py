def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict

    left = 0
    max_freq = 0
    freqs = defaultdict(int)
    max_length = 0

    for right in range(len(s)):
        freqs[s[right]] += 1
        max_freq = max(max_freq, freqs[s[right]])
        
        if (right - left + 1) - max_freq > k:
            freqs[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Test cases for validation
assert characterReplacement("ABAB", 2) == 4
assert characterReplacement("AABABBA", 1) == 4
