def pivote(array, start, end):
    pivote = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivote:
            high = high - 1
        while low <= high and array[low] <= pivote:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
def quicksort(array, start, end):
    if start >= end:
        return
    p = pivote(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)
lista = [10,5,6,9,2,50,80]
quicksort(lista,0,len(lista)-1)
print(lista)