def recBinarySearch(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list)//2
        
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recBinarySearch(list[mid+1:], target)
            else:
                return recBinarySearch(list[:mid], target)

def verify(result):
    print("target: ", result)

n = [1,2,3,4,5,6,7,8,9,10]
result = recBinarySearch(n, 12)
verify(result)
result = recBinarySearch(n, 4)
verify(result)