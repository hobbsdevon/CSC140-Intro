from mpi4py import MPI
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
	numList = createList(12)
	print(numList)
	splitList = splitList(numList)
	
data = comm.scatter(splitList, root = 0)
#print('process', rank, 'has', data)
sums = comm.gather(sumOfList(data), root = 0)
#print(sums)

if rank == 0:
	finalSum = sumOfList(sums)
	print(finalSum)


