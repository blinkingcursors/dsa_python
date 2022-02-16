'''
implementation of insertion sort ascending order
blog post: www.blinkingcursors.in/dsa/insertion_sort
'''

import random


random_array = []
for i in range(1, 11):
    random_array.append(random.randint(-100000000, 100000000))


def insertion_sort_ascending(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j-1
        while i >=0 and list[i] > key:
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list

def insertion_sort_descending(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j-1
        while i >=0 and list[i] < key:
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list


if __name__ == '__main__':
    # list = [5, 2, 4, 6, 1, 3]
    print("Unsorted list:", random_array)
    print("Sorted list ascending:", insertion_sort_ascending(random_array))
    print("Sorted list descending:", insertion_sort_descending(random_array))