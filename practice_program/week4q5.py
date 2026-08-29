def rotatearray(nums, k):
    k = k % len(nums)
    n=len(nums)
    newarray=[0]*n
    for i in range(n):
        newarray[(i+k)%n]=nums[i]
    return newarray
nums=[1,2,3,4,5,6,7]
k=3
print(rotatearray(nums,k))