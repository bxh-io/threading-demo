# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time

N = 10000000

def calculate_cube(num):
    """
    function to cal cube of given num
    """
    for i in range(num):
        _ = num * num * num


if __name__ == "__main__":
    start_time = time.perf_counter()
    # creating thread
    t1 = threading.Thread(target=calculate_cube, args=(int(N/2),))
    t2 = threading.Thread(target=calculate_cube, args=(int(N/2),))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    elapsed_time = time.perf_counter() - start_time
    print(f"\n Threaded cube took: {elapsed_time:0.4f} seconds \n ")
