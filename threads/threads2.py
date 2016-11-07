# multiproc_test.py

import random
import multiprocessing


def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a 
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())
	
	return out_list

if __name__ == "__main__":
	print(multiprocessing.cpu_count())
	size = 5   # Number of random numbers to add
	procs = 6   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 
	jobs = []
	manager = multiprocessing.Manager()
	out_list= manager.list()
	for i in range(0, procs):
		
		process = multiprocessing.Process(target=list_append, 
			                              args=(size, i, out_list))
		jobs.append(process)
		

	# Start the processes (i.e. calculate the random number lists)		
	for j in jobs:
		j.start()

	# Ensure all of the processes have finished
	for j in jobs:
		j.join()
		#print(j)

	print (out_list)
