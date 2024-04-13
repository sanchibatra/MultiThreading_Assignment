import numpy as np
import matplotlib.pyplot as plt
import time
import threading
import pandas as pd

def matrix_multiplication(constant_matrix, num_threads):
    results = []
    for _ in range(10):
        start_time = time.time()
        threads = []
        batch_size = 100 // num_threads
        for i in range(0, 100, batch_size):
            thread = threading.Thread(target=perform_multiplication, args=(constant_matrix, results, i, min(i+batch_size, 100)))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        end_time = time.time()
        results.append(end_time - start_time)
    return np.mean(results)


def perform_multiplication(constant_matrix, results, start_idx, end_idx):
    for i in range(start_idx, end_idx):
        random_matrix = np.random.rand(1000, 1000)
        result = np.matmul(random_matrix, constant_matrix)


constant_matrix = np.random.rand(1000, 1000)


thread_counts = list(range(1, 11))
times = []
for num_threads in thread_counts:
    avg_time = matrix_multiplication(constant_matrix, num_threads)
    times.append(avg_time)
    print(f"Time taken with {num_threads} threads: {avg_time} seconds")


data = {'Number of Threads': thread_counts, 'Average Time (seconds)': times}
df = pd.DataFrame(data)


df.to_csv('multithreading.csv', index=False)

plt.plot(thread_counts, times)
plt.xlabel('Number of Threads')
plt.ylabel('Average Time (seconds)')
plt.title('Time Taken vs Number of Threads')
plt.show()

# Display the DataFrame
print(df)
