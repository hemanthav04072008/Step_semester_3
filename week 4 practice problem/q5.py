def rotate_array(nums, k):
    if not nums:
        return nums

    n = len(nums)
    k = k % n
    new_array = [0] * n

    for i in range(n):
        new_position = (i + k) % n
        new_array[new_position] = nums[i]

    return new_array


nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter rotation positions: "))

print(rotate_array(nums, k))