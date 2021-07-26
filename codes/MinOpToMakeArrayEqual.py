def getMinOps(n: int) -> int:
    arr = []
    for n in range(n):
        arr.append(n*2+1)
    print("Input array: ", arr)

getMinOps(10)

# n % 2 == 0
# 1 + 3 + 5 + ... + (n-2)
