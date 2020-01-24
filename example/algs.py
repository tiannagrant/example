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

def bubblesort_counter(B):
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
   
    
    

def quicksort(A):
    assignment_counter=0
    conditional_counter=0
    assignment_counter+=1
    conditional_counter+=1
    if len(A) <= 1:
        return A
    L = []
    R = []
    assignment_counter+=2
    p =  np.random.choice(range(len(A))) # random pivot
    E = [A[p]] # this is a list of all the things that are equal to the pivot.
    assignment_counter+=3
    conditional_counter+=3
    for i in range(len(A)):
        if i == p:
            continue
        if A[i] < A[p]:
            L.append(A[i])
        elif A[i] > A[p]:
            R.append(A[i])
        else:
            E.append(A[i])
    return quicksort(L) + E + quicksort(R)



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