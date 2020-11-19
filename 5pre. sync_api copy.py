#import asyncio
import random
import requests
import time

def query_api():
#async def query_db():
    """
    Faux API call
    """
    rand = random.uniform(0, 2.0)
    time.sleep(rand)
    #asyncio.sleep(rand)
    return {"movie": "Star Wars"}

def main():
#async def main():
    result = query_api()
    #result = await query_db()

if __name__ == "__main__":
    start_time = time.perf_counter()

    r = main()
    #r = asyncio.run(main())

    elapsed_time = time.perf_counter() - start_time
    print(f"\n Sync API call took {elapsed_time:0.4f} seconds \n ")
