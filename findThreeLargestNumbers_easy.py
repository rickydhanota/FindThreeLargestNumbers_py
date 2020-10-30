#Find the 3 largest numbers
#Write a function that takes in an array of at least 3 integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

#The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12]

#array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
#[18, 141, 541]

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1): #python its exclusive so we have to do idx+1 to account for the range function
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))