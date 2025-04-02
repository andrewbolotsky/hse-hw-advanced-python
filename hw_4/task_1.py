import multiprocessing
import threading
import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def run_and_time(n: int, individual_times: list[float]):
    start = time.time()
    print(f"Running fib")
    fib(n)
    end = time.time()
    print(f"End running fib in time: {end - start}")
    individual_times.append(end - start)


def threading_execution(n, times=10):
    threads = []
    individual_times = []
    start_time_total = time.time()

    for _ in range(times):
        thread = threading.Thread(target=run_and_time, args=(n, individual_times))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    total_time = time.time() - start_time_total
    return individual_times, total_time


def multiprocessing_execution(n, times=10):
    processes = []
    individual_times = multiprocessing.Manager().list()
    start_time_total = time.time()

    for _ in range(times):
        process = multiprocessing.Process(target=run_and_time, args=(n, individual_times))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_time = time.time() - start_time_total
    return list(individual_times), total_time


if __name__ == "__main__":
    n = 37
    times = 10

    print(f"Running via threading")
    threading_times, threading_total = threading_execution(n, times)
    print(f"End running via threading")
    print(f"Running via multiprocessing")
    multiprocessing_times, multiprocessing_total = multiprocessing_execution(n, times)
    print(f"End running via multiprocessing")

    result = f"""
Fibonacci Calculation Comparison (n = {n}, runs = {times})

=== Threading Execution ===
Individual times (sec): {[round(t, 2) for t in threading_times]}
Total time: {round(threading_total, 2)} sec

=== Multiprocessing Execution ===
Individual times (sec): {[round(t, 2) for t in multiprocessing_times]}
Total time: {round(multiprocessing_total, 2)} sec

=== Summary ===
1. Threading total time: {round(threading_total, 2)} sec
3. Multiprocessing total time: {round(multiprocessing_total, 2)} sec
"""
    with open("artifacts/task_1/task_1.txt", "w", encoding="utf-8") as file:
        file.write(result)

    print(result)
