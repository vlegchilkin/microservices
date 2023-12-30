from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log
from ..common.router import router as common_router

router = APIRouter(prefix="/toliman", tags=["toliman"])
router.include_router(common_router)


@router.on_event("startup")
async def startup_event():
    log.info("Toliman startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Toliman shutdown completed")


@router.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Toliman"})
