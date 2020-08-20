# Assignment 2
# Algorithms and Data Structures 1
# 1DL210
# 2019 uppsala university
# Author: Rex Ruan
# Implementation of heap sort

import time

def swap(index1,index2,A):
    copyValue = A[index1]
    A[index1] = A[index2]
    A[index2] = copyValue
    return A


def maxheapify(i,A,heapsize):
    #if len(A) > 2*i+1:
    rightIndex = 2*i+2
    #if len(A) > 2*i:
    leftIndex = 2*i+1
    if leftIndex < heapsize:
        if A[leftIndex] > A[i]:
            largest = leftIndex
        else:
            largest = i
    else:
        largest = i

    if rightIndex < heapsize:
        if A[rightIndex] > A[largest]:
            largest = rightIndex

    if largest != i:
        swap(i,largest, A)
        maxheapify(largest,A,heapsize)

def buildMaxHeap(A):
    startIndex = (len(A)-2)//2
    for i in range(startIndex,-1,-1):
        maxheapify(i,A,len(A))

def heapSort(A):
    buildMaxHeap(A)
    heapsize = len(A)-1
    for i in range(len(A)-1,0,-1):
        swap(0,i,A)
        maxheapify(0,A,heapsize)
        heapsize -= 1

