def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # kurangi i karna elemen terbesar sudah pasti berada di posisi paling kanan, jadi tak perlu diperiksa
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [1, 7, 4, 2]

bubble_sort(arr)

print(arr)