import asyncio
import random
import time
import pprint


async def query_db(x:int) -> dict:
    rand = random.uniform(0, 2.0)
    await asyncio.sleep(rand)
    return {"movie": "Star Wars", "call":x}

async def main():
    tasks = [query_db(1), query_db(2)]

    # Waiting
    finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for x in finished:

        result = x.result()

        print("\n", result, "\n")
        return

if __name__ == "__main__":
    starting_time = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - starting_time
    print(f"\n API call took {elapsed:0.2f} seconds \n")
