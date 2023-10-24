def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict

    # Hash map to store groups of anagrams
    anagrams = defaultdict(list)

    for word in strs:
        # Use sorted tuple of characters as the key
        key = tuple(sorted(word))
        anagrams[key].append(word)

    # Return the grouped anagrams
    return list(anagrams.values())

# Test cases for validation
assert set(tuple(sorted(group)) for group in groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == set([("bat",), ("nat", "tan"), ("ate", "eat", "tea")])
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]
