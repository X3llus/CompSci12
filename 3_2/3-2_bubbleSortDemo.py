#Bubble Sort Demo - Sorts a list from low to high

#Variables
numbers = [99, 90, 80, 70, 60, 50, 40, 30, 20, 10] #The list!
swap = 0 #Used in the swapping places of numbers.

#Code to do the Bubble Sort
for i in len(numbers):                  #Repeat 10x.
    for j in range (len(numbers)-1):            #Repeat 9x.
        if numbers[j] > numbers[j+1]:     #If 1st # > 2nd # then...
            swap = numbers[j+1]           #swap the position of the #s.
            numbers[j+1] = numbers[j]
            numbers[j] = swap

#Print the sorted list
for k in len(numbers):
    print numbers[k]
