from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log
from .details import router as details_router
from ..common.router import router as common_router

router = APIRouter(prefix="/proxima-centauri", tags=['Proxima Centauri'])
router.include_router(common_router)
router.include_router(details_router)


@router.on_event("startup")
async def startup_event():
    log.info("Proxima Centauri startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Proxima Centauri shutdown completed")


@router.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Proxima Centauri"})
