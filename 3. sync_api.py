import random
import requests
import time

def query_api():
    """
    Faux API call
    """
    rand = random.uniform(0, 2.0)
    time.sleep(rand)
    return {"movie": "Star Wars"}

def main():
    result = query_api()

if __name__ == "__main__":
    start_time = time.perf_counter()

    r = main()

    elapsed_time = time.perf_counter() - start_time
    print(f"\n Sync API call took {elapsed_time:0.4f} seconds \n ")
