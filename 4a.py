def InsertionSort(lst):
    i = 0
    while i < len(lst):
        small = lst[i]
        for j in range(i + 1, len(lst)):
            nxt = lst[j]
            if small > nxt:
                small = lst[j]
        index = lst.index(small)
        if i == index:
            pass
        else:
            lst.remove(small)
            lst.insert(i, small)
        i += 1
    return lst

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
    return arr

if __name__ == '__main__':
    lst = []
    n = int(input("Enter the size of the list: "))
    print("Enter", n, "numbers for the list:")
    for i in range(n):
        lst.append(int(input()))
    print(lst)

    print("Enter 1 for Insertion Sort, 2 for Merge Sort")
    ch = int(input())
    if ch == 1:
        lst = InsertionSort(lst)
        print("The sorted array is:", lst)
    elif ch == 2:
        lst = mergeSort(lst)
        print("The sorted array is:", lst)
    else:
        print("Invalid choice")
