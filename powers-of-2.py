n = int(input())

def powerOf2(n):
    return 0 if n == 1 else len(format(n, "b"))

print(powerOf2(n))
