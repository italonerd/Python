# multiproc_test.py
import time
import random
import multiprocessing


def list_append(timeToWait, id, out_list):
	"""
	Creates an empty list and then appends a 
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
        print "Start thread id:",id
	time.sleep(timeToWait*10)
        #
        print "Stop thread id:",id
        
if __name__ == "__main__":
	size = 10000000   # Number of random numbers to add
	procs = 10   # Number of processes to create
        
        print "Create a list of jobs"
	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 
	jobs = []
	for i in range(0, procs):
		out_list = list()
                time_to_wait = random.randrange(1,4)
		process = multiprocessing.Process(target=list_append, 
			                              args=(time_to_wait, i, out_list))
		jobs.append(process)
        print "Start the processes"
	# Start the processes (i.e. calculate the random number lists)		
	for j in jobs:
		j.start()
        
        print "Ensure all of the processes have finished"
	# Ensure all of the processes have finished
	for j in jobs:
            j.join()

	print "List processing complete."