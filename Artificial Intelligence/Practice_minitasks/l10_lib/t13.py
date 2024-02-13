
import timeit


def sum_numbers():
    return sum(range(1, 1001))


execution_time = timeit.timeit(sum_numbers, number=100000)

print(f"Execution time for sum_numbers function: {execution_time:.5f} seconds")
