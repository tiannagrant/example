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
    
    
    #Duplicted assert statement
    #assert np.array_equal(algs.bubblesort([4,4,5,5,7,7,1,1])), np.array(([1,1,4,4,5,5,7,7]))
    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
   

def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
   
