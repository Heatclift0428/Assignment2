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

        else:
            print("please enter a value within the range")

    except ValueError:
        print("please enter a valid number")
