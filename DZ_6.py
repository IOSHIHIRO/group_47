def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr,value):
    n = len(arr)
    low = 0
    high = len(arr) - 1
    mid = len(arr) // 2
    resultOK = False

    while arr[mid] != value and low <= high:
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if value == arr[mid]:
        resultOK = True

    if resultOK == True:
        print(f'ID of {value} == {mid}')
    else:
        print('No velue')

my_list = [50, 26, 7, 22, 10, 77,99,101,33]
sorted_list = selection_sort(my_list)
print(sorted_list)
print(binary_search(my_list,50))


