#Implementation of Insertion Sort algorithm in Python:-
#This is done by (M.G.Mohankumar)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#This function will sort an input list arr using the Insertion Sort algorithm.

#Now that we've implemented the sorting algorithm, please let me know if you'd like to proceed with the next steps of your assignment or if you have any specific questions about the implementation.