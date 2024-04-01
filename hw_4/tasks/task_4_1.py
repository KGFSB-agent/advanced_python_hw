import threading
import time
from multiprocessing import Process
from os import path

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    start_time = time.perf_counter()
    for _ in range(10):
        fibonacci(32)
    end_time = time.perf_counter()
    result_sync = f"Затраченное время на выполнение вычислений синхронно: {end_time - start_time} сек"

    start_time = time.perf_counter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fibonacci, args=(32, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.perf_counter()
    result_threads = f"Затраченное время на выполнение вычислений с потоками: {end_time - start_time} сек"
    print(result_threads)

    processes = []

    start_time = time.perf_counter()
    for _ in range(10):
        process = Process(target=fibonacci, args=(32,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
    end_time = time.perf_counter()
    result_processes = f"Затраченное время на выполнение вычислений с процессами: {end_time - start_time} сек"

    with open(path.join("artifacts", "artifacts_4_1", "artifact_4_1.txt"), "w") as file:
        file.write("\n".join((result_sync, result_threads, result_processes)))