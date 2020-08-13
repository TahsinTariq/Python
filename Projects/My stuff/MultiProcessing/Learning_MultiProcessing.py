import multiprocessing
import time

start = time.perf_counter()

def delay(seconds):
	print(f"Start Sleep")
	time.sleep(seconds)
	print(f"Done Sleep")

if __name__ == '__main__':

	# p1 = multiprocessing.Process(target = delay, args =[5])
	# p2 = multiprocessing.Process(target = delay, args = [5])

	# p1.start()
	# p2.start()

	# p1.join()
	# p2.join()
	processes = []
	for _ in range(10):
		p = multiprocessing.Process(target = delay,args = [1])
		p.start()
		processes.append(p)

	for p in processes:
		p.join()

	finish = time.perf_counter()
	print(f"Finished in {round(finish-start,4)} seconds")