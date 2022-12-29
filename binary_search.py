def binarySearch(list, target):
    fr = 0
    ls = len(list) - 1

    while fr <= ls:
        mid = (fr + ls)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            fr = mid + 1
        else:
            ls = mid - 1

    return None

def verify(index):
    if index is not None:
        print(index)
    else:
        print("Not found in the list")

n = [1,2,3,4,5,6,7,8,9,10]

result = binarySearch(n, 3)

verify(result)