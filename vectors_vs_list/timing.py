import time

tic = time.perf_counter()
print(tic)
#perform any calculation
sum = 0
for i in range(1000000):
    sum+=i
#Re-run timing
toc = time.perf_counter()
print(f"Performed calculation in {toc - tic:0.4f} seconds")