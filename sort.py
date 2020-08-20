import os
import array
import sys
import random
from rangen import rangen
import time #import time to calculate running time
from heapSort import heapSort

# Bubble Sort
# This is the system's sorting algorithm that you use to compare with your result

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False

#Insertion Sort
def insertionsort(a):
	for j in range(1,len(a)):
		key=a[j]
		i=j-1
		while i>=0 and a[i]>key:
			a[i+1]=a[i]
			i=i-1

		a[i+1]=key

#create an array with random number given its maximal number as the size of the array
def generateArray(size):
    return [random.randint(0,size) for _ in range(size)]

# This is the function to verify your implemented sorting algorithm
# You need to change it a bit to call your sorting algorithm
def test():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)

    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    #unsortedLists = [generateArray(number) for number in maxNumbers]

    # sort the array using bubblesort and calculate running time
    start=time.time()
    bubblesort(a)# You need to change here to call your sorting algorithm
    end=time.time()
    print("Bubblesort running time:   ",round(end-start,4));
    nums.close()

    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    #sort the array using insertionsort and calculate running time
    start=time.time()
    insertionsort(a)
    end=time.time()
    print("Insertionsort running time:  ",round(end-start,4));


    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    #sort the array using insertionsort and calculate running time
    start=time.time()
    heapSort(a)
    end=time.time()
    print("Heapsort running time: ",round(end-start,4));
    # output nums_sorted.txt
    nums_sorted = open('nums_sorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

    # compare your result (nums_sorted.txt) against the result of bubblesorting algorithm (nums_ref.txt)
    os.system('sort -n nums.txt > nums_ref.txt')
    ret = os.system('diff nums_sorted.txt nums_ref.txt > tmp.txt')

    # output result
    if int(ret) == 0:
        print ("Sorted!")

    if int(ret) != 0:
        print ("Not sorted!")

# run 5 times for each sort algorithm given different sample size
# from 10**3 to 10**5
if __name__ == "__main__":
    for maxNumber in [10**i for i in range(3,6)]: #give maximal number and the size of the array
        for i in range(5): #run 5 times for each category
            print("Size %d and the number of running time is %d" %(maxNumber,i))
            rangen(maxNumber)
            test()

