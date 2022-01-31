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
    n = len(nums)
    low = 0
    high = n
    mid = n//2
    while -1 < mid < n:
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
        if mid == (low + high)//2:
            break
        else:
            mid = (low + high)//2
    return -1



if __name__ == '__main___':
    print(binarySearchRec([1,3,4,5,6,7,9,10,11], 5))
    print(binarySearchIter([1,3,4,5,6,7,9,10,11], 5))
    print(binarySearchRec([i for i in range(0, 200, 2)], 130))
    print(binarySearchIter([i for i in range(0, 200, 2)], 130))
