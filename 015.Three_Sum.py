def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return result

# Test cases for validation
assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([0,1,1]) == []
assert threeSum([0,0,0]) == [[0,0,0]]
