def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = False # pakai flag mendeteksi apakah ada pertukaran dalam pass ini
        for j in range(n - i - 1): # kurangi 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True #true kan karna ada pertukaran
        
        if not flag: break #skip, artinya array sudah terurut

arr = [1, 7, 4, 2]

bubble_sort(arr)

print(arr)