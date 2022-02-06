import asyncio
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_504_GATEWAY_TIMEOUT
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app.server.routes.domains import router as DomainsRouter

REQUEST_TIMEOUT_ERROR = 10

app = FastAPI()

app.add_middleware(PrometheusMiddleware, app_name="redsift-test", group_paths=True, prefix='redsift',
                   buckets=[0.1, 0.25, 0.5])
app.add_route("/metrics", handle_metrics)

app.include_router(DomainsRouter, tags=["Domains"], prefix="/domains")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Redsift hiring assigment"}


# Kinda experimental solution for set global timeout: https://github.com/tiangolo/fastapi/issues/1752#issuecomment-682579845
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
