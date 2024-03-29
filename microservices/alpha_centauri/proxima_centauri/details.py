from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log


def build_router():
    return APIRouter(prefix="/details")


router = build_router()


@router.on_event("startup")
async def startup_event():
    log.info("Proxima Centauri (Details) startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Proxima Centauri (Details) shutdown completed")


@router.get("/xxx")
async def root(request: Request):
    return JSONResponse(content={"owner": "Proxima Centauri (Details)"})
