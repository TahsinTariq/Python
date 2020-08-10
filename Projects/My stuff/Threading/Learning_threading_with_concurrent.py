import time
import concurrent.futures

start = time.perf_counter()

def delay(seconds : float):
	print(f"Start Sleep")
	time.sleep(seconds)
	return "Done Sleep"

with concurrent.futures.ThreadPoolExecutor() as e:
	# can also do results = e.map(delay, [i for i in range(10)])
	# but this will not print as they are completed.
	results = [e.submit(delay,1) for _ in range(10)]
	for f in concurrent.futures.as_completed(results):
		print(f.result())
	# f1 = e.submit(delay,1)
	# print(f1.result())

finish = time.perf_counter()
print(f"Finished in {round(finish-start,4)} seconds")