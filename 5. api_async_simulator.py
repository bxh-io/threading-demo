import asyncio
import random
import time
import requests
import pprint


async def query_db():
    rand = random.uniform(0, 2.0)
    await asyncio.sleep(rand)
    return {"movie": "Star Wars"}

async def main():
    result = await query_db()
    pprint.pprint(result)

if __name__ == "__main__":
    s = time.perf_counter()

    r = asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"API call took {elapsed:0.2f} seconds")
