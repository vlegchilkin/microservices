import mscom.config as microservice_config
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log
from mscom.actuator.router import router
from ..rigil_kentaurus.router import router as rigil_kentaurus_router
from ..toliman.router import router as toliman_router
from ..proxima_centauri.router import router as proxima_centauri_router
from ..common.router import router as common_router
from ..common import some  # noqa: F401


def build_application():
    fast_api = FastAPI(title="Alpha Centauri")
    fast_api.include_router(common_router)
    return fast_api


app = build_application()
app.include_router(router)
app.include_router(rigil_kentaurus_router, prefix="/rigil-kentaurus", tags=["Rigil Kentaurus"])
app.include_router(toliman_router)
app.include_router(proxima_centauri_router)


@app.on_event("startup")
async def startup_event():
    log.info(f"Initializing Alpha Centauri on port {microservice_config.microservice_settings.server_port}")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down Alpha Centauri")


@app.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Alpha Centauri"})
