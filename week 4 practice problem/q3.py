def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


nums = list(map(int, input("Enter array elements: ").split()))
print(contains_duplicate(nums))