def selection_sort(arr):

    # [10 , 5, 7, 8, 12]
    # [5, 10, 7, 8, 12]
    # [5, 7, 10, 8, 12]
    # [5, 7, 8, 10, 12]

    n = len(arr)

    for i in range(n):
        min_index = i 

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j 

        arr[i], arr[min_index] = arr[min_index], arr[i]

        # 10 , 5 = 5, 10

        # 1 , 10 = 10 , 1

        # best case = O(n2)
        # average case = O(n2)
        # worst case = O(n2)


    return arr 

lis = [10, 5, 8, 7, 12]
print(selection_sort(lis))

def insertion_sort(arr):

    # [10, 5, 8, 7, 12]

    # [5, 8, 7, 12, 10]

    # [5, 7, 12, 10, 8]

    # [5, 7, 10, 8, 12]

    # [5, 7, 8, 10, 12]

    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key 

    return arr 

lis = [10, 5, 8, 7, 12]
print(insertion_sort(lis))



        



