import time

#Start timing
start = time.perf_counter()
#perform any calculation
sum = 0
for i in range(1000000):
    sum+=i
#Re-run timing
end = time.perf_counter()
print(f"Performed calculation in {end - start:0.4f} seconds")