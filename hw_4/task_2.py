from __future__ import annotations

import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Callable, Type, List, Tuple
import time
import os


def compute_chunk(start_idx: int, end_idx: int, a: float, step: float, f: Callable[[float], float]) -> float:
    acc = 0.0
    for i in range(start_idx, end_idx):
        acc += f(a + i * step) * step
    return acc


def integrate(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    n_jobs: int = 1,
    n_iter: int = 10_000_000,
    executor: Type[ThreadPoolExecutor | ProcessPoolExecutor]
) -> float:
    step = (b - a) / n_iter
    total_iterations = n_iter
    chunk_size = total_iterations // n_jobs
    remainder = total_iterations % n_jobs

    chunks: List[Tuple[int, int]] = []
    start = 0
    for i in range(n_jobs):
        end = start + chunk_size
        if i < remainder:
            end += 1
        chunks.append((start, end))
        start = end

    with executor(max_workers=n_jobs) as exec_instance:
        futures = [
            exec_instance.submit(compute_chunk, start, end, a, step, f)
            for (start, end) in chunks
        ]
        results = [future.result() for future in futures]

    return sum(results)


def compare_executors() -> None:
    func = math.cos
    a, b = 0, math.pi / 2
    n_iter = 10_000_000
    max_workers = os.cpu_count()*2
    with open("artifacts/task_2/task_2.txt", "w") as file:
        file.write("n_jobs \t\t ThreadPoolExecutor \t\t ProcessPoolExecutor\n")
        for n_jobs in range(1, max_workers + 1):
            print("Start to run ThreadPoolExecutor")
            start_time = time.time()
            integrate(func, a, b, n_jobs=n_jobs, n_iter=n_iter, executor=ThreadPoolExecutor)
            thread_time = time.time() - start_time
            print("Start to run ProcessPoolExecutor")
            start_time = time.time()
            integrate(func, a, b, n_jobs=n_jobs, n_iter=n_iter, executor=ProcessPoolExecutor)
            process_time = time.time() - start_time
            file.write(f"n_jobs={n_jobs}\t ThreadPool={thread_time:.6f}s\t ProcessPool={process_time:.6f}s\n")
            print(f"Count of jobs={n_jobs}, ThreadPool={thread_time:.6f}s, ProcessPool={process_time:.6f}s")


if __name__ == "__main__":
    compare_executors()