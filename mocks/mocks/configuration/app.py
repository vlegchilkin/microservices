import mscom.config as microservice_config
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log

app = FastAPI(title="Mock Services")


@app.on_event("startup")
async def startup_event():
    log.info(f"Initializing Mock Services on port {microservice_config.microservice_settings.server_port}")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down Mock Services")


@app.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Mock Services"})
