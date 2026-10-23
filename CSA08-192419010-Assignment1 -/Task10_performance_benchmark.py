# Task 10 - Performance and Scaling Benchmark
import time
import milkrate

for n in [300, 6000, 150000]:
    t0 = time.perf_counter()
    tot = sum(milkrate.payout(10, 4.2, 8.7) for _ in range(n))
    t1 = time.perf_counter()
    print(f"N={n:6d} Total={tot:12.2f} Time={t1-t0:.5f}s")
