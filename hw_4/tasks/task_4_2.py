import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from os import path

def single_step(f, a, step, i):
    return f(a + i * step) * step

def integrate_range(args):
    f, a, step, start, end = args
    return sum(single_step(f, a, step, i) for i in range(start, end))

def integrate(f, a, b, *, n_jobs=1, n_iter=20000000, executor=ThreadPoolExecutor):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    args = [(f, a, step, i * chunk_size, min((i + 1) * chunk_size, n_iter)) for i in range(n_jobs)]

    with executor(max_workers=n_jobs) as executor:
        results = list(executor.map(integrate_range, args))

    return sum(results)

if __name__ == '__main__':
    n_jobs = os.cpu_count() * 2

    output = ''

    for jobs in range(1, n_jobs + 1):
        start = time.perf_counter()
        integrate(math.cos, 0, math.pi / 2, n_jobs=jobs, executor=ThreadPoolExecutor)
        end = time.perf_counter()
        output += f'[Потоки] n_jobs: {jobs} | Время: {end - start}\n'

    output += '\n======================\n'
    for jobs in range(1, n_jobs + 1):
        start = time.perf_counter()
        integrate(math.cos, 0, math.pi / 2, n_jobs=jobs, executor=ProcessPoolExecutor)
        end = time.perf_counter()
        output += f'\n[Процессы] n_jobs: {jobs} | Время: {end - start}'

    with open(path.join("artifacts", "artifacts_4_2", "artifact_4_2.txt"), 'w') as file:
        file.write(output)


