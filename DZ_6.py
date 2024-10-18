def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr):
    value = 22
    low = 0
    high = len(arr) - 1
    mid = len(arr) // 2

    while arr[mid] != value and low <= high:
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return 'No value'
    else:
        return 'ID =', mid

my_list = [50, 26, 7, 22, 10, 77,99,101,33]
sorted_list = selection_sort(my_list)
print(sorted_list)
print(binary_search(sorted_list))