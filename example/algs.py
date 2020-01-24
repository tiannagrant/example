import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(B):
    assignment_counter=0
    conditional_counter=0
    index_length = len(B) -1
    assignment_counter+=1
    sorted = False
    assignment_counter+=1
    while not sorted:
        sorted = True
        assignment_counter+=1
        conditional_counter+=1
        for i in range(0, index_length):
            assignment_counter+=1
            conditional_counter+=1
            if B[i] > B[i+1]:
                sorted = False
                assignment_counter+=3
                B[i], B[i+1] = B[i+1], B[i]
    print("number of assignments=", assignment_counter)
    print("number of conditonals=", conditional_counter)
    return B



    

def quicksort(x):
    assignment_counter = 0
    conditional_counter = 0
    assignment_counter += 2
    length = len(sort)
    conditional_counter+=1
    if length <= 1:
        return sort
    else:
        assignment_counter+=1
        #remove and return- from the end of the list
        pivot = sort.pop()
    items_greater = []
    items_lower = []
    for item in sort:
        assignment_counter+=4
        conditional_counter+=1
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)
    print("number of assignments=", assignment_counter)
    print("number of conditional=", conditional_counter)

    return quicksort(items_lower) + [pivot] +quicksort(items_greater)


def InsertionSort(A):
    assignment_counter = 0
    conditional_counter = 0
    assignment_counter+=2
    B = [None for i in range(len(A))] # B is a blank list of the same length as A
    for x in A:
        assignment_counter+=4
        conditional_counter+=2
        for i in range(len(B)):
            if B[i] == None or B[i] > x:
                # then x goes in spot i, and we should move everything over.
                j = len(B)-1
                while j > i:
                    assignment_counter+=3
                    B[j] = B[j-1]
                    j -= 1
                B[i] = x
                break # okay we are done placing x
    print(assignment_counter)
    print(conditional_counter)
    return B

A = [3, 5, 4, 2, 6, 7, 1, 8]
B = InsertionSort(A)