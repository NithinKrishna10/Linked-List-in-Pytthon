
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # If x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1



def lenier_serch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1,2,3,4,5,6,7,8,9]
b=binary_search(arr,7)
print(lenier_serch(arr,6))
print(b)

