import threading
import time

start = time.perf_counter()

def delay(seconds : float):
	print(f"Start Sleep")
	time.sleep(seconds)
	print(f"Done Sleep")

t1 = threading.Thread(target = delay, args = [1.5])
t2 = threading.Thread(target = delay, args = [1.5])

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,4)} seconds")