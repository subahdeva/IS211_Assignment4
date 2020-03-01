#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time

def sequential_search(seq, lookup):
    start = time.time()
    idx = 0
    fn = -1
    while idx < len(seq):
        if seq[idx] == lookup:
            fn = idx
            break
        else:
            idx += 1
    end = time.time()
    return (fn, end - start)


def ordered_sequential_search(seq, item):
    seq.sort()
    start = time.time()
    idx = 0
    fn = -1
    while idx < len(seq):
        if seq[idx] == item or seq[idx] > item:
             fn = idx
             break
    end = time.time()
    return (fn, end - start)


def binary_search_iterative(seq, item):
    start = time.time()
    top = 0
    bottom = len(seq) - 1
    fn = -1
    if bottom != 0:
        while top < bottom:
            middle = (top + bottom) // 2
            if seq[middle] == item:
                fn = middle
                break
            elif item < seq[middle]:
                bottom = middle - 1
            else:
                bottom = middle + 1
    end = time.time()
    return (fn, end - start)


def binary_search_recursive(seq, item):
    start = time.time()
    fn = -1
    stop = False
    if len(seq) == 0:
        stop = True
    if not stop:
        mid = len(seq) // 2
        if seq[mid] == item:
            fn = mid
            stop = True
        elif item < seq[mid]:
            return binary_search_recursive(seq[:mid], item)
        else:
            return binary_search_recursive(seq[mid + 1:], item)

    end = time.time()
    return (fn, end - start)


if __name__ == '__main__':
    import random
    from data import *
    
    stats = {'seq': 0.0,
             'oseq': 0.0,
             'bin': 0.0,
             'rbin': 0.0}

    for n, nums in SEQ.iteritems():
        print 'Size: ', n
        length = len(nums)

        for count in xrange(101):
            stats['seq'] += sequential_search(nums, -1)[1]
            stats['oseq'] += ordered_sequential_search(nums, -1)[1]
            stats['bin'] += binary_search_iterative(nums, -1)[1]
            stats['rbin'] += binary_search_iterative(nums, -1)[1]
        print 'Count: ', count
        for key, stat in stats.iteritems():
            search_type = 'Sequential Search'
            if key == 'oseq':
                search_type = 'Ordered Sequential Search'
            elif key == 'bin':
                search_type = 'Iterative Binary Search'
            elif key == 'rbin':
                search_type = 'Recursive Binary Search'
            print search_type + ' took %10.7f seconds to run, on average' % (stat / length)



# In[ ]:





# In[ ]:




