 # This is Question 3 of Assignment 2
# Francis Apurado
#Lotto award checking system
import random

PWNs = []
SWNs = []
PlayerDetails = []
PlayerNum = []

def insertionSort(array, size):
    for x in range(1, size):
        key = array[x]
        y = x - 1

        # comparing the key array with each element on the left side until a smaller number is found
        while y >= 0 and key < array[y]:
            array[y + 1] = array[y]
            y = y - 1

        array[y + 1] = key

rand = random.sample(range(1, 30), 8)


for i in range(len(rand)):
    x = rand[i]
    if i <= 7 and i <=5 :
        PWNs.append(x)
    if i >=6 :
        SWNs.append(x)


while True:

    try:
        Menu = int(input("1. Show Initialized data\n"
                           "2. Display Statistics\n"
                           "3. Check my lotto status\n"
                           "4. Exit\n"
                           ))

        if Menu == 1:
            print("Showing data")
            print("PWNs: ", PWNs)
            print("SWNs: ", SWNs)

        if Menu == 2:
            print("Displaying statistics")

        if Menu == 3:
            print("Checking lotto status")

        if Menu == 4:
            print("program ending.......")
            quit()


    except ValueError:
        print("Please provide an integer")




