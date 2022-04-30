 # This is Question 3 of Assignment 2
# Francis Apurado
#Lotto award checking system

PWNs = []
SWNs = []
PlayerDetails = []
PlayerNum = []

while True:

    try:
        Menu = int(input("1. Show Initialized data\n"
                           "2. Display Statistics\n"
                           "3. Check my lotto status\n"
                           "4. Exit\n"
                           ))

        if Menu == 1:
            print("Showing data")

        if Menu == 2:
            print("Displaying statistics")

        if Menu == 3:
            print("Checking lotto status")

        if Menu == 4:
            print("program ending......")
            quit()


    except ValueError:
        print("Please provide an integer")




