#!/usr/bin/env python
# coding: utf-8

from mpi4py import MPI
import os
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def createList(size):
	returnList = []
	random.seed(time.time)
	for i in range(size):
		returnList.append(random.randint(0, size))
	return returnList
	
def sumOfList(lst):
	sum = 0
	for ele in lst:
		sum += ele
	return sum
	
def splitList(lst):
	returnList = []
	partialSize = int(len(lst)/size)
	start = 0
	end = partialSize
	for partialList in range(size):
		returnList.append(lst[start:end])
		start += partialSize
		end += partialSize
	return returnList


	

if rank == 0:
	finalSum = 0
	testList = createList(8)
	print(testList)
	partialIndex = 1
	fullList = splitList(testList)
	print(fullList)
	for proc in range(1, size):
		comm.send(fullList[partialIndex],dest = proc)
		partialIndex += 1
		tempSum = comm.recv(source = proc)
		proc0Sum = sumOfList(fullList[0])
		finalSum += tempSum
		finalSum += proc0Sum
	print(finalSum)	
else:
	#for proc in range(1, size):
	partialList = comm.recv(source = 0)
	partialSum = sumOfList(partialList)
	comm.send(partialSum, dest = 0)
			

'''
finalSum = 0
for proc in range(1, 4):
	tempSum = comm.recv(source = proc)
	for ele in tempSum:
		finalSum += tempSum
'''
	








