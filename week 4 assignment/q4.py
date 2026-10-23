def subarray_sum(nums, k):
    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        count += prefix_count.get(current_sum - k, 0)

        prefix_count[current_sum] = (
            prefix_count.get(current_sum, 0) + 1
        )

    return count


nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter target sum: "))

print(subarray_sum(nums, k))