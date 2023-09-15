import time

def create_and_update_list():
    return 0

def create_and_update_vector():
    return 0

#Start timing
startlist = time.perf_counter()

#perform any calculation

#Re-run timing
endlist = time.perf_counter()

#Start timing
startvector = time.perf_counter()

#perform any calculation

#Re-run timing
endvector = time.perf_counter()
print(f"Performed calculation in {endlist - startlist:0.4f} seconds")
print(f"Performed calculation in {endvector - startvector:0.4f} seconds")

