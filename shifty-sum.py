n = int(input())
k = int(input())


def shiftySum(n, k):
    nums = []
    nums.append(n)
    for i in range(1, k + 1):
        nums.append(n * (10 ** i))
        #print(nums)
    return sum(nums)
print(shiftySum(n, k))
