import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?
    

    B = np.array([3,5,4,2,6,7,1,8])
    assert np.array_equal(np.array(algs.bubblesort(B)), np.array([1, 2, 3, 4, 5, 6, 7, 8]))
    empty = np.array([])
    assert np.array_equal(np.array(algs.bubblesort(empty)), np.array([]))
    duplication = np.array([4,4,5,5,7,7,1,1])
    assert np.array_equal(np.array(algs.bubblesort(duplication)), np.array([1, 1, 4, 4, 5, 5, 7, 7]))
    
    #list with odd number of elements
    odd = np.array([1,3,2,4,9])
    assert np.array_equal(np.array(algs.bubblesort(odd)), np.array([1,2,3,4,9]))
                    
    #list with characters
                    
    a = np.array(['apple', 'banana','zebra', 'red'])
    assert np.array_equal(np.array(algs.bubblesort(a)), np.array(['apple', 'banana', 'red', 'zebra']))
    
   

   

def test_quicksort():
    
    A = np.array([3, 5, 4, 2, 6, 7, 1, 8])
    assert np.array_equal(np.array(algs.quicksort(A)), np.array([1, 2, 3, 4, 5, 6, 7, 8]))
  
    
    #Empty array
    empty = np.array([])
    assert np.array_equal(np.array(algs.quicksort(empty)), np.array([]))
    
    #Duplication array
    duplication = np.array([4,4,5,5,7,7,1,1])
    assert np.array_equal(np.array(algs.quicksort(duplication)), np.array([1, 1, 4, 4, 5, 5, 7, 7]))
    
    #list with odd number of elements
    odd = np.array([1,3,2,4,9])
    assert np.array_equal(np.array(algs.quicksort(odd)), np.array([1,2,3,4,9]))
                    
    #list with characters
                    
    a = np.array(['apple', 'banana','zebra', 'red'])
    assert np.array_equal(np.array(algs.quicksort(a)), np.array(['apple', 'banana', 'red', 'zebra']))


def test_InsertionSort():
    A = np.array([3, 5, 4, 2, 6, 7, 1, 8])
    assert np.array_equal(np.array(algs.InsertionSort(A)), np.array([1, 2, 3, 4, 5, 6, 7, 8]))
  
    
    #Empty array
    empty = np.array([])
    assert np.array_equal(np.array(algs.InsertionSort(empty)), np.array([]))
    
    #Duplication array
    duplication = np.array([4,4,5,5,7,7,1,1])
    assert np.array_equal(np.array(algs.InsertionSort(duplication)), np.array([1, 1, 4, 4, 5, 5, 7, 7]))
    
    #list with odd number of elements
    odd = np.array([1,3,2,4,9])
    assert np.array_equal(np.array(algs.InsertionSort(odd)), np.array([1,2,3,4,9]))
                    
    #list with characters
                    
    a = np.array(['apple', 'banana','zebra', 'red'])
    assert np.array_equal(np.array(algs.InsertionSort(a)), np.array(['apple', 'banana', 'red', 'zebra']))
    
   
