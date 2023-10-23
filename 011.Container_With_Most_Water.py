def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        min_height = min(height[left], height[right])
        width = right - left
        max_area = max(max_area, min_height * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Test cases
assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([1,1]) == 1
