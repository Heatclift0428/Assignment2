# This is Question 2 of Assignment 2
# Francis Apurado


import random

while True:
    try:
        UserChoice = float(input("1. Test an individual sorting algorithm \n "
                                 "2. Test Multiple sorting algorithms\n"))

        if UserChoice == 1:
            pass
            break

        if UserChoice == 2:

            AlgorithmChoice = float(input("1. selection sort \n"
                                          "2. insertion sort \n"
                                          "3. merge sort \n"
                                          "4. quick sort \n "
                                          "5. counting sort \n"))

            arraySize = int(input("please enter the size of the array"))

            RandomArray = []

            for i in range(arraySize):
                x = random.randint(0, 100)
                RandomArray.append(x)

            break

        else:
            print("please enter a value within the range")

    except ValueError:
        print("please enter a valid number")
