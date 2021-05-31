def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        left = lista[:mid]
        right = lista[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        ll=len(left)  
        lr=len(right)     
        while i < ll and j < lr:
            if left[i] < right[j]:
                lista[k]=left[i]
                i=i+1
            else:
                lista[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            lista[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            lista[k]=right[j]
            j=j+1
            k=k+1

lista = [10,5,6,9,2,50,80]
mergeSort(lista)
print(lista)