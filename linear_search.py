def linearSearch(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(index)
    else:
        print("Not found in the list")

n = [1,2,3,4,5,6,7,8,9,10]

result = linearSearch(n, 3)

verify(result)