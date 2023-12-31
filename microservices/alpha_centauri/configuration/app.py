import mscom.config as microservice_config
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log
from mscom.actuator.router import router as actuator_router
from ..rigil_kentaurus.router import router as rigil_kentaurus_router
from ..toliman.router import router as toliman_router
from ..proxima_centauri.router import router as proxima_centauri_router
from ..common.router import router as common_router

app = FastAPI(title="Alpha Centauri")
app.include_router(actuator_router)
app.include_router(common_router)
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
