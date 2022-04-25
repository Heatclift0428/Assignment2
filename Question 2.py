# This is Question 2 of Assignment 2
# Francis Apurado

import random


# selection sort algorithm
def SelectionSort(array, size):
    for x in range(size):
        minIndex = x

        for y in range(x + 1, size):

            if array[y] < array[minIndex]:  # will select the minimum for each loop #sorts in Ascending
                minIndex = y

        (array[x], array[minIndex]) = (array[minIndex], array[x])  # append the minimum in the right position


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

        mid = len(array) // 2   # middle of the array
        Left = array[:mid]
        Right = array[mid:]

        mergeSort(Left)    # sorting left side
        mergeSort(Right)   # sorting right side

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

        while j < len(Right):   # Checks if any elements in the Right array is left
            array[k] = Right[j]
            j += 1
            k += 1


while True:
    try:
        UserChoice = float(input("1. Test an individual sorting algorithm\n"
                                 "2. Test Multiple sorting algorithms\n"))

        if UserChoice == 2:
            pass
            break

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


        else:
            print("please enter a value within the range")

    except ValueError:
        print("please enter a valid number")
