#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/user/bin/env python
# -*- Coding: utf-8 -*-

import time


def insertion_sort(random_list):
    start = time.time()
    for index in range(1, len(random_list)):
        current_value = random_list[index]
        position = index
        while position > 0 and random_list[position - 1] > current_value:
            random_list[position] = random_list[position - 1]
            position = position - 1
            random_list[position] = current_value
    end = time.time()
    return (end - start)


def gap_insertion_sort(random_list, start, gap):
    for i in range(start + gap, len(random_list), gap):
        current_value = random_list[i]
        position = i
        while position >= gap and random_list[position - gap] > current_value:
            random_list[position] = random_list[position - gap]
            position = position - gap
            random_list[position] = current_value


def shell_sort(random_list):
    start = time.time()
    list_count = len(random_list) // 2
    while list_count > 0:
        for position in range(list_count):
            gap_insertion_sort(random_list, position, list_count)
        list_count //= 2
    end = time.time()
    return (end - start)


def python_sort(random_list):
    start = time.time()
    random_list.sort()
    end = time.time()
    return (end - start)


if __name__ == '__main__':
    from data import *

    stats = {'Insertion Sort': 0.0,
             'Shell Sort': 0.0,
             'Python Sort': 0.0}

    for key, items in SEQ.iteritems():
        length = len(items)
        print 'Size: ', key
        for count in xrange(101):
            stats['Insertion Sort'] += insertion_sort(items)
            stats['Shell Sort'] += shell_sort(items)
            stats['Python Sort'] += python_sort(items)

        for sort_type, stat in stats.iteritems():
            print sort_type + ' took %10.7f seconds to run, on average' % (stat/length)


# In[ ]:




