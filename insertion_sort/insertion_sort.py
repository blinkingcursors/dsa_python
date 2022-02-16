'''
implementation of insertion sort ascending order
blog post: www.blinkingcursors.in/dsa/insertion_sort
'''

import random


random_array = []
for i in range(1, 11):
    random_array.append(random.randint(-100000000, 100000000))


def insertion_sort(list):
    for j in range(1, len(list)):
        # print("j:", j)
        key = list[j]
        # print("key:", key)
        i = j-1
        # print("i:", i)
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list


if __name__ == '__main__':
    print("Unsorted list:", random_array)
    print("Sorted list:", insertion_sort(random_array))
