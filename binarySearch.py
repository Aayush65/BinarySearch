from os import system
system("cls")

# Recursive Function
def binarySearchRec(A: list, x: int) -> int:
    n = len(A)
    i = n//2
    if 0 <= i < n:
        if x < A[i]:
            return binarySearchRec(A[:i], x)
        elif x > A[i]:
            index = binarySearchRec(A[i+1:], x)
            return i + index + 1  if index > -1 else -1
        elif x == A[i]:
            return i
    return -1

# Iterative Function
def binarySearchIter(A: list, x: int) -> int:
    n = len(A)
    high = 0
    mid = n//2
    low = n-1
    while 0 <= mid < n:
        mid = (high + low + 1)//2
        if x < A[mid]:
            low = mid - 1
        elif x > A[mid]:
            high = mid
        else:
            return mid
    return -1


if __name__ == '__main___':
    print(binarySearchRec([1,3,4,5,6,7,9,10,11], 5))
    print(binarySearchIter([1,3,4,5,6,7,9,10,11], 5))
    print(binarySearchRec([i for i in range(0, 200, 2)], 130))
    print(binarySearchIter([i for i in range(0, 200, 2)], 130))