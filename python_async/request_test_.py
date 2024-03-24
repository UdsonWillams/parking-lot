from time import time
import aiohttp
import asyncio
import requests
import httpx

url = "https://www.python.org/"

async def main_aiohttp():

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200

initial_time = time()
for i in range(1, 100):
    asyncio.run(main_aiohttp())
final_time = time() - initial_time
elapsed_time = round(final_time, 3)
print(f"TEMPO DECORRIDO COM AIOHTTP: {elapsed_time}")

async def main_httpx_async():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        assert response.status_code == 200    

initial_time = time()
for i in range(1, 100):
    asyncio.run(main_httpx_async())
final_time = time() - initial_time
elapsed_time = round(final_time, 3)
print(f"TEMPO DECORRIDO COM HTTPX ASYNC: {elapsed_time}")

def main_httpx_sync():
    with httpx.Client() as client:
        response = client.get(url)
        assert response.status_code == 200    

initial_time = time()
for i in range(1, 100):
    main_httpx_sync()
final_time = time() - initial_time
elapsed_time = round(final_time, 3)
print(f"TEMPO DECORRIDO COM HTTPX NÃO-ASYNC: {elapsed_time}")

def main_requests_lib():
    with requests.Session() as client:
        response = client.get(url)
        assert response.status_code == 200    

initial_time = time()
for i in range(1, 100):
    main_requests_lib()
final_time = time() - initial_time
elapsed_time = round(final_time, 3)
print(f"TEMPO DECORRIDO COM REQUESTS NÃO-ASYNC: {elapsed_time}")
