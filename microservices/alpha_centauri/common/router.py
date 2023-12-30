from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from microservices.alpha_centauri import log

router = APIRouter(prefix="/common")


@router.on_event("startup")
async def startup_event():
    log.info("Common startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Common shutdown completed")


@router.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Common"})
