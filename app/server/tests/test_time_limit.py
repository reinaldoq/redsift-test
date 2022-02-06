import asyncio
import time

import pytest
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from httpx import AsyncClient
from starlette.status import HTTP_504_GATEWAY_TIMEOUT

REQUEST_TIMEOUT_ERROR = 1  # Threshold

app = FastAPI()  # Fake app


# Creating a test path
@app.get("/test_path")
async def route_for_test(sleep_time: float) -> None:
    await asyncio.sleep(sleep_time)


# Adding a middleware returning a 504 error if the request processing time is above a certain threshold
@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        start_time = time.time()
        return await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT_ERROR)

    except asyncio.TimeoutError:
        process_time = time.time() - start_time
        return JSONResponse({'detail': 'Request processing time excedeed limit',
                             'processing_time': process_time},
                            status_code=HTTP_504_GATEWAY_TIMEOUT)


# Testing wether or not the middleware triggers
@pytest.mark.asyncio
async def test_504_error_triggers():
    # Creating an asynchronous client to test our asynchronous function
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test_path?sleep_time=3")
    content = eval(response.content.decode())
    assert response.status_code == HTTP_504_GATEWAY_TIMEOUT
    assert content['processing_time'] < 1.1


# Testing middleware's consistency for requests having a processing time close to the threshold
@pytest.mark.asyncio
async def test_504_error_consistency():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        errors = 0
        sleep_time = REQUEST_TIMEOUT_ERROR * 0.9
        for i in range(100):
            response = await ac.get("/test_path?sleep_time={}".format(sleep_time))
            if response.status_code == HTTP_504_GATEWAY_TIMEOUT:
                errors += 1
        assert errors == 0
