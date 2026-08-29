def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return([i],[j])
num=[2,7,4,5,9]
target=9
print(twosum(num,target))