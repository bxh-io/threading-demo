# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time
import random

def query_api():
    """
    Faux API call
    """
    rand = random.uniform(0, 2.0)
    time.sleep(rand)
    return {"movie": "Star Wars"}


if __name__ == "__main__":
    start_time = time.perf_counter()
    # creating thread
    t1 = threading.Thread(target=query_api)
    t2 = threading.Thread(target=query_api)

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
    print(f"\n Threaded API took: {elapsed_time:0.4f} seconds \n ")
