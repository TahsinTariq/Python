import time
import concurrent.futures

start = time.perf_counter()

def delay(seconds : float, num):
	print(f"Start Sleep for {num}")
	time.sleep(seconds)
	return f"Done Sleep for {num}"
if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as e:
		# can also do results = e.map(delay, [i for i in range(10)])
		# but this will not print as they are completed.
		results = [e.submit(delay,1, i) for i in range(10)]
		for f in concurrent.futures.as_completed(results):
			print(f.result())
		# f1 = e.submit(delay,1)
		# print(f1.result())

	finish = time.perf_counter()
	print(f"Finished in {round(finish-start,4)} seconds")