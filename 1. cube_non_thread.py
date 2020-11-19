# Python program to illustrate the concept
# of threading
# importing the threading module
import time

N = 10000000

def calculate_cube(num):
    """
    Function to calculate cube of given number
    """
    for i in range(num):
        _ = num * num * num


if __name__ == "__main__":
    start_time = time.perf_counter()

    # creating cube directly
    _ = calculate_cube(N)

    # both threads completely executed
    elapsed_time = time.perf_counter() - start_time
    print(f"\n Threaded cube took: {elapsed_time:0.4f} seconds \n ")
