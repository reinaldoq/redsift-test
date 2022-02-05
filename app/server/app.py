import asyncio
import logging
import time


from starlette_exporter import PrometheusMiddleware, handle_metrics

from fastapi import FastAPI, Request
from fastapi_utils.timing import add_timing_middleware
from starlette.staticfiles import StaticFiles

from app.server.routes.domains import router as DomainsRouter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(PrometheusMiddleware, app_name="redsift-test", group_paths=True, prefix='redsift', buckets=[0.1, 0.25, 0.5])
app.add_route("/metrics", handle_metrics)

app.include_router(DomainsRouter, tags=["Domains"], prefix="/domains")

add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")
static_files_app = StaticFiles(directory=".")
app.mount(path="/static", app=static_files_app, name="static")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Redsift hiring assigment"}