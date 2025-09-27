# take input 
n = int(input())
k = int(input())


def shiftySum(n, k):
    #init list
    nums = []
    #adf fist num 
    nums.append(n)
    # add a 0 to n, k times 
    for i in range(1, k + 1):
        nums.append(n * (10 ** i))
        #print(nums)
    return sum(nums)
print(shiftySum(n, k))
