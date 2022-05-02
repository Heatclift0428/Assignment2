 # This is Question 3 of Assignment 2
# Francis Apurado
#Lotto award checking system
import random
import sys
sys.setrecursionlimit(10000)

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index



def insertionSort(array, size):
    for x in range(1, size):
        key = array[x]
        y = x - 1

        # comparing the key array with each element on the left side until a smaller number is found
        while y >= 0 and key < array[y]:
            array[y + 1] = array[y]
            y = y - 1

        array[y + 1] = key

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def SelectionSort(array, size):
    for x in range(size):
        minIndex = x

        for y in range(x + 1, size):

            if array[y] < array[minIndex]:  # will select the minimum for each loop #sorts in Ascending
                minIndex = y
        swap(array, minIndex, x)


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

# Pre-initilization phase

PWNs = []
SWNs = []
PlayerNum = []
count = 1

for i in range(1000):
    x = random.sample(range(1,30), 6)
    mergeSort(x)
    PlayerNum.append([[count], x])
    count = count + 1

randlotto = random.sample(range(1, 30), 8)
PWNs = randlotto[0:6]
SWNs = randlotto[6:8]

insertionSort(PWNs, len(PWNs))
SelectionSort(SWNs, len(SWNs))

print(PlayerNum[0][1])
print(PWNs)
print(SWNs)

First = 0
Second = 0
Third = 0
Fourth = 0

for x in range(1000):
    P = 0
    S = 0
    print(PlayerNum[x][1])
    for i in range(6):
        result = BinarySearch(PlayerNum[x][1], PWNs[i])
        if result != -1:
            print("Primary Element is present")
            P = P+1
        else:
            print("Primay Element is not present in array")

    for y in range (2):
        otherResult = BinarySearch(PlayerNum[x][1],SWNs[y])
        if otherResult != -1:
            print("Secondary Element is present")
            S = S + 1
        else:
            print("Secondary Element is not present in array")

    if P == 6:
        First = First + 1

    elif P == 5:
        Second = Second + 1

    elif P == 4:
        Third = Third + 1

    elif P == 3 & S == 2:
        Fourth = Fourth + 1


while True:

    try:
        Menu = float(input("1. Show Initialized data\n"
                           "2. Display Statistics\n"
                           "3. Check my lotto status\n"
                           "4. Exit\n"
                           ))

        if Menu == 1:
            print("Showing data")
            print("PWNs: ", PWNs)
            print("SWNs: ", SWNs)

        elif Menu == 2:
            print("Displaying statistics.....\n")
            print("Winners Statistics Table:\n")
            print("Winner Class   | Total Number of Winners\n")
            print("1st Class:             ",First                  )
            print("2nd Class:             ",Second)
            print("3rd Class:            ", Third)
            print("4th Class:            ", Fourth)

        elif Menu == 3:
            PW = 0
            SW = 0
            userChoice = int(input("Enter the ID: "))
            userChoice = userChoice - 1

            for i in range(6):
                result = BinarySearch(PlayerNum[x][1], PWNs[i])
                if result != -1:
                    PW = PW + 1

            for y in range(2):
                otherResult = BinarySearch(PlayerNum[x][1], SWNs[y])
                if otherResult != -1:
                    SW = SW + 1

            print("Player's ID: ", PlayerNum [userChoice][0], "\n")
            print("Player Game Numbers", PlayerNum[userChoice][1], "\n")
            print("PWNs: ", PW, "\n")
            print("SWNs: ", SW, "\n")
            print("Players Status: ")

            if P == 6:
                print("You are a 1st Class winner")

            elif P == 5:
                print("You are a 2nd Class Winner ")

            elif P == 4:
                print("You are a 3rd Class Winner")

            elif P == 3 & S == 2:
                print("You are a 4th Class Winner")

            else:
                print("You are not a Winner")


        elif Menu == 4:
            print("program ending.......")
            quit()


    except ValueError:
        print("Please provide an integer")




