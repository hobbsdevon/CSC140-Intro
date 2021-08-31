'''
Dependant: Reading the file, split by new line
Independant: Split by whitespace, Counting each instance

'''

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	sampleFile = open('sampleFile.txt', 'r').read()
	fileOut = open('fileOut.txt', 'w')
	lineList = sampleFile.split("\n")
	partialListSize = int(len(lineList)/size)
	start = 0
	end = partialListSize
	#count instances of first part
	instances = dict()
	for line in lineList[start:end]:
		line = line.strip()
		words = line.split()
		for word in words:
			if word in instances:
				instances[word] = instances[word] + 1
			else:
				instances[word] = 1	
	#Send some lines to each process
	for proc in range(1, size):
		start += partialListSize
		end += partialListSize
		comm.send(lineList[start:end], dest = proc)
	#Recieve and merge dictionaries
	for proc in range(1, size):
		intermediateDict = comm.recv(source = proc)
		for ele in intermediateDict:
			if ele in instances:
				instances[ele] = instances[ele] + 1
			else:
				instances[ele] = 1
	
else:
	lineList = comm.recv(source = 0)
	intermediateDict = dict()
	for line in lineList:
		line = line.strip()
		words = line.split()
		for word in words:
			if word in intermediateDict:
				intermediateDict[word] = intermediateDict[word] + 1
			else:
				intermediateDict[word] = 1
	comm.send(intermediateDict, dest = 0)
if rank == 0:	
	fileOut.write(str(instances))
	#fileOut.close()
	#sampleFile.close()
	print(instances)
