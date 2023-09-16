import time
import numpy as np

#Size of lengths to initialize and declare for both the list and vector
size = 10_000_0000

def create_and_update_list():
    listfiller = []
    for i in range(size):
        listfiller.append(i)

def create_and_update_vector():
    arr = np.empty(size)
    for i in range(size):
        arr[i] = i

#Start timing
startlist = time.perf_counter()

#perform any calculation
create_and_update_list()
#Re-run timing
endlist = time.perf_counter()

#Start timing
startvector = time.perf_counter()

#perform any calculation
create_and_update_vector()
#Re-run timing
endvector = time.perf_counter()
print(f"Performed calculation in {endlist - startlist:0.4f} seconds")
print(f"Performed calculation in {endvector - startvector:0.4f} seconds")
