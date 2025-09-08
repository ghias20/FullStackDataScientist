def second_largest(nums):
    unique_nums=list(set(nums))
    unique_nums.sort(reverse=True)
    if len(unique_nums)<2:
        return None
    return unique_nums[1]
print(second_largest([10, 5, 20, 8]))
