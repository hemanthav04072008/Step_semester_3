def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


nums = list(map(int, input("Enter rotated sorted array: ").split()))
print(find_min(nums))