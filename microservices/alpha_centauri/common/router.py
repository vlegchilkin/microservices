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


# !!!!
# All functions here have the same name, and it works cause the name doesn't matter.
# We are not calling them directly, it used only for openapi spec as description.
# !!!!


@router.get("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "GET"})


@router.head("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "HEAD"})


@router.post("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "POST"})


@router.put("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "PUT"})


@router.delete("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "DELETE"})


@router.options("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "OPTIONS"})


@router.trace("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "TRACE"})


@router.patch("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "PATCH"})
