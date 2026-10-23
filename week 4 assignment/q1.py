def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Forward pass: product of elements to the left
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Backward pass: multiply by product of elements to the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


nums = list(map(int, input("Enter array elements: ").split()))
print(product_except_self(nums))