# This is Question 2 of Assignment 2
# Francis Apurado

import random
import time
import sys

sys.setrecursionlimit(10000)


def SelectionSort(array, size):
    for x in range(size):
        minIndex = x

        for y in range(x + 1, size):

            if array[y] < array[minIndex]:  # will select the minimum for each loop #sorts in Ascending
                minIndex = y
        swap(array, minIndex, x)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def insertionSort(array, size):
    for x in range(1, size):
        key = array[x]
        y = x - 1

        # comparing the key array with each element on the left side until a smaller number is found
        while y >= 0 and key < array[y]:
            array[y + 1] = array[y]
            y = y - 1

        array[y + 1] = key


def mergeSort(array):
    if len(array) > 1:

        mid = len(array) // 2  # middle of the array
        Left = array[:mid]
        Right = array[mid:]

        mergeSort(Left)  # sorting left side
        mergeSort(Right)  # sorting right side

        i = j = k = 0

        # Temporary Arrays
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):  # Checks if any elements in the Left array is left
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):  # Checks if any elements in the Right array is left
            array[k] = Right[j]
            j += 1
            k += 1


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(list):
    quickSortHelper(list, 0, len(list) - 1)


def quickSortHelper(list, left, right):
    if left < right:
        pivotIndex = partition(list, left, right)
        quickSortHelper(list, left, pivotIndex - 1)
        quickSortHelper(list, pivotIndex + 1, right)


def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 101

    for z in range(0, size):
        count[array[z]] += 1

    for z in range(1, 101):
        count[z] += count[z - 1]

    z = size - 1
    while z >= 0:
        output[count[array[z]] - 1] = array[z]
        count[array[z]] -= 1
        z -= 1

    for z in range(0, size):
        array[z] = output[z]


# main of the program
while True:
    try:
        UserChoice = float(input("1. Test an individual sorting algorithm\n"
                                 "2. Test Multiple sorting algorithms\n"))

        if UserChoice == 1:

            AlgorithmChoice = float(input("1. selection sort \n"
                                          "2. insertion sort \n"
                                          "3. merge sort \n"
                                          "4. quick sort \n "
                                          "5. counting sort \n"))

            arraySize = int(input("please enter the size of the array\n"))

            RandomArray = []

            for i in range(arraySize):
                x = random.randint(0, 100)
                RandomArray.append(x)

            if AlgorithmChoice == 1:
                print("Not sorted: ", RandomArray)
                SelectionSort(RandomArray, len(RandomArray))
                print('Sorted: ', RandomArray)

            if AlgorithmChoice == 2:
                print("Not sorted: ", RandomArray)
                insertionSort(RandomArray, len(RandomArray))
                print('Sorted: ', RandomArray)

            if AlgorithmChoice == 3:
                print("Not sorted: ", RandomArray)
                mergeSort(RandomArray)
                print('Sorted: ', RandomArray)

            if AlgorithmChoice == 4:
                print("Not sorted: ", RandomArray)
                quickSort(RandomArray)
                print('Sorted: ', RandomArray)

            if AlgorithmChoice == 5:
                print("Not sorted: ", RandomArray)
                countingSort(RandomArray)
                print('Sorted: ', RandomArray)

        if UserChoice == 2:

            arraySize = int(input("please enter the size of the array\n"))

            RandomArray = []

            for i in range(arraySize):
                x = random.randint(0, 100)
                RandomArray.append(x)

            print("Not sorted: ", RandomArray)

            SArray = RandomArray
            start = time.time() * 1000
            SelectionSort(SArray, len(SArray))
            print('Sorted (Selection): ', SArray)
            end = time.time() * 1000
            print('Run time ', end - start, " ms")

            IArray = RandomArray
            start = time.time() * 1000
            insertionSort(IArray, len(IArray))
            print('Sorted (Insertion): ', IArray)
            end = time.time() * 1000
            print('Run time ', end - start, " ms")

            MArray = RandomArray
            start = time.time() * 1000
            mergeSort(MArray)
            print('Sorted (Merge): ', MArray)
            end = time.time() * 1000
            print('Run time ', end - start, " ms")

            QArray = RandomArray
            start = time.time() * 1000
            quickSort(QArray)
            print('Sorted (Quick): ', QArray)
            end = time.time() * 1000
            print('Run time ', end - start, " ms")

            CArray = RandomArray
            start = time.time() * 1000
            countingSort(CArray)
            print('Sorted (Counting): ', CArray)
            end = time.time() * 1000
            print('Run time ', end - start, " ms")


        else:
            print("please enter a value within the range")

    except ValueError:
        print("please enter a valid number")
